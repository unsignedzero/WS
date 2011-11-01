
r"""
# WonderSwan 
# By David Tran (unsignedzero)
# 11-01-2011
# Version 0.8.3.0
# Provides basic meta programming support to python "format"

Abstract:
The purpose of this code is to provide a set of functions for
formatting, debugging and related purposes for programmers.
Each function has specific requirements that can be different
from other functions, so read about it before using it. As 
with other Python Scripts, this can be executed directly.
In this case it will run the formatter function.
"""

#DO NOT CHANGE BELOW THIS POINT

class ZText_Error ( Exception ):
  r"""
  ZText_Error

      Base class for exceptions in this module
  """
  
  pass

class UnbalancedBraces ( ZText_Error ):
  r"""
  UnbalancedBraces

      Exception for unbalanced braces for this module.

      ARGUMENTS:
        expr -- Input expression in which the error occurred

        msg  -- explanation of the error
        
  """

  def __init__(self, expr, msg):
    self.expr = expr
    self.msg = msg

def pause():
  r"""
  pause()
      pause()

      Correct pauses regardless of the os this function is running on.
  """
  #import os,sys
  #pau = "pause" if sys.platform[:3]=="win" else 
    #"read -rsn 1 -p \"Press any key to continue...\\n\""
  #os.system(pau)
  
  raw_input("Press any key to continue...\n")

#def formatter( fname, fout = None, space_count = 2, 
  #*kargs, special = 0, EXCEPTION = True ):
def formatter( fname, fout = None, space_count = 2, 
  special = 0, EXCEPTION = True ):
  r""":w
  formatter(...)
     formatter( fname, fout = None, space_co unt = 2, 
       *kargs, special = 0, EXCEPTION = True )

     Given a correct filename fname, this program auto-formats the program 
     file. This function formats source code, in a similar fashion to    
     Python, in which "proper" matching spacing is applied for each line 
     between an opening and closing brace. 

     fname is the ONLY required argument. If fout is not defined, the
     output will have the same name as the input file except now with 
     "_edit.txt" appended to it.

     ASSUMPTIONS:
       The file passed should have balanced braces. If this requirement is   
       not met, the program will return an Exception, unless NO_EXCEPTIONS
       is true!

       All lines of the source code can and will be "reorder" even if they
       are comments!

     ARGUMENTS:

       fname        -- This is the name of input file.

     Optional Arguments:

       fout         -- This is the name of the output file. 
         If not specified, then it will be fname + "_edit.txt"

       space_count  -- This is the amount of spaces, that each 
         opening brace will shift the lines below it. Default 2.

      Optional Keyword Arguments:

        special      -- special arguments, see special section below.

        EXCEPTION    -- Disables exceptions messages of unbalanced braces.
       
      SPECIAL:
        Treat this variable as an array of bools.  (Represented as an  
          integer) This turns on/off additional functions, listed below.
        
         1 -- Comments after the end brace, what the opening brace was
        
         2 -- Use tabs, rather than spaces!

         4 -- Treat /* */ comments as braces, for the purposes of     
               indentation

         8 -- Comment-only // lines are shifted -1 left

        16 -- Non-braced, if/for/while will indent
        
  """
  
  import sys
  
  shift       = 0
  shift_delay = 0   #For   4
  cond_shift  = 0   #For  16
  cond_delay  = 0   #For  16
  mline_shift = 0   #Future Use
  brace_start = '{'
  brace_end   = '}'
  stack       = []  #For   1
  space_char  = ' ' #For   2

  #Files 
  source_code = open(fname)
  fout = (fname + "_edit.txt") if (fout == None) else fout 
  dest_code   = open(fout, "w" )
  ###err_code    = open(fname + "_err.txt", "w" )

  print("%s starting with %s. \nOutput is %s." % 
    (sys._getframe(0).f_code.co_name , fname, fout) )

  #SPECIAL
  if special & 2 :
    space_char = '\t'

  for (count,line) in enumerate(source_code) :

     ###err_code.write( '%03d | ' % len(line.strip() ) + line)

    #Empty Line are Empty
     empty_line = 1 if line.strip() else 0
   
     line = ( ( empty_line * ( shift + cond_shift + mline_shift  )*  
              space_count * space_char                            ) 
              + line.strip()                                      )
              
    #Insert Extra Formatting here
     if special > 0:
       if special & 1 :
         if brace_start in line and brace_end not in line :
           stack.append( line[:-1].strip() )
         elif brace_start not in line and brace_end in line :
           line += " // " + stack.pop()
       if special & 4 :      
         if r'/*' in line:
           shift_delay +=1
         if r'*/' in line:
           shift_delay -=1
       if special & 8 :
         if (line.lstrip()).startswith('//'):
           if (line[0] == ' ' or line[0] == '\t' ): #CHECK ME
             line = line[1:]
       if special & 16:
         if ( 'if' in line or 'else' in line 
          or 'for' in line or 'while' in line ) and brace_start not in line:
           cond_shift = 1
         else:
           cond_shift = 0
           
    #Write to File
     dest_code.write( line + '\n' )

    ##Calculate Shift for next line
     if brace_start in line :
       shift += 1
     if brace_end   in line :
       shift -= 1
     if shift_delay != 0    :
       shift += shift_delay
       shift_delay = 0
       
     #Check if negative shift
     if EXCEPTION and shift < 0 :
       print( "\n  File \"%s\", line %i, in %s" % 
         ( fname, count,  sys._getframe().f_code.co_name ) )
       raise UnbalancedBraces( 0 , "Unbalanced Closing Braces in the file" )
       
  #Check if there is extra shift at end.
  if EXCEPTION and shift != 0:
    print( "\n  File \"%s\" , in %s" % 
      ( fname,  sys._getframe().f_code.co_name ) )
    raise UnbalancedBraces( 0 , "Unbalanced Opening Braces in the file!" )
  print( "%s Compeleted!" % sys._getframe(0).f_code.co_name )

#def lcount( fname , fout = None, width = 6, *kargs, code = "UTF-8" ) :
def lcount( fname , fout = None, width = 6, code = "UTF-8" ) :
  r"""
  lcount(...)
     lcount( fname , fout = None, width = 6, *kargs, code = "UTF-8" )

     Writes the line number of each line into the output text file.



       fname -- This is the name of input file.
       
       fout  -- This is the name of the output file. If not specified,
         then it will be fname + "_counted.txt"
         
       width -- Sets the width of the number column
       
       code  -- Sets the default coding of the file

  """

  import sys

  #Files
  file_in  = open(fname, "r", 1, code)
  fout = (fname + '_counted.txt') if (fout == None) else fout 
  file_out = open(fout,"w" , 1, code)

  print("%s starting with %s. Output is %s." % 
    (sys._getframe(0).f_code.co_name , fname, fout) )
    
  width = "%0" + str(width) + "d | "

  for (count,line) in enumerate(file_in) :
    file_out.write( str( width % count) + line )  

  print( "%s Compeleted!" % sys._getframe(0).f_code.co_name )  

def rspace_killer ( fname, fout = None ) :
  r"""
  rspace_killer(...)
     rspace_killer ( fname, fout = None )
     
     Removes excess white space on the right
     
     ARGUMENTS:
     
     fname -- This is the name of the input file.
     
     fout  -- This is the name of the output file. If not specified,
       then it will be fname + "_wk.txt"     
  """

  import sys
  
  fin = open(source,"r")
  fout = source + '_wk.txt' if ( fout == None ) else fout
  dest = open(fout,"w")

  print("%s starting with %s. Output is %s." % 
    (sys._getframe(0).f_code.co_name , fname, fout) )
    
  for line in fin :
    fout.write( line.rstrip() )
    
  print( "%s Compeleted!" % sys._getframe(0).f_code.co_name ) 

if __name__ == "__main__" :
  import sys
  print("Starting WS")
  try:
    #We test and see if, upon execution, some arguments are passed.
    #
    #Written this way, the code will run, if at least one argument is
    #passed. The other parameter(s), will be default ones.
    #If not, we will load our manual CLI prompt to get the needed 
    #information from the user
    inf = sys.argv[1]
    outf = (sys.argv[1] + "_edit.txt") if ( 
      len(sys.argv[1:2]) == 1 ) else sys.argv[2]
    spf = 0 if ( len(sys.argv[1:3]) < 3 ) else sys.argv[3]
  except IndexError:
    #We are in the CLI Prompt
    finput = raw_input("Please enter a file name\n")
    finput = finput.split()
    try:
      #Sets default values BEFORE getting it from input. Done this way,
      #both variables will have default starting values before
      #we try to fill it in.
      foutput = None
      mode = 0
      foutput = str(finput[1])
      mode = int(finput[2])
    except IndexError:
      pass
    finally:
      if ( foutput == '0' ) :
        #'0' is an escape variable that can be typed in as input and
        #remapped to None, so that the programmer can use the default 
        #output file
        foutput = None
      if ( isinstance(finput,list) ) :
        #Note that strings can be accessed as lists with the [] operator
        #so we must check if the input is a legit list or just an array
        #of chars!
        formatter(finput[0], foutput, special = int(mode))
      else :
        formatter(finput, special = 0)
  else:
    #We got some arguments passed in on run time. Don't use internal prompt.
    if ( outf == '0' ) :
      #Like above '0' is the escape value for default, for the 2nd argument
      outf = None
    formatter(inf,outf, special = spf)
  pause()
  