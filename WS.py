# WonderSwan
# Provides basic meta programing support
# to python "format"
# 07-24-2011
# Version 0.5
# 10-08-2011
# Version 0.8

#DO NOT CHANGE BELOW THIS POINT

class ZText_Error(Exception):
				  """Base class for exceptions in this module"""
  pass

class UnbalancedBraces(ZText_Error):
				  """Exception for unbalanced braces
  Attributes:
					    expr -- input expression in which the error occurred
    msg  -- explanation of the error
  """
  def __init__(self, expr, msg):
					    self.expr = expr
    self.msg = msg

def pause():
				  """Correct pauses regardless of the os this function is running on."""
  import os,sys
  pau = "pause" if sys.platform[:3]=="win" else "read -sn 1 -p \"Press any key to continue...\\n\""
  os.system(pau)
  
def formatter( fname, fout = None, space_count = 2, *kargs, special = 0 NO_EXCEPTION = False ):
				  r"""
  formatter(...)
     formatter( fname, fout = None, space_co unt = 2, *kargs, special = 0, NO_EXCEPTION = False )

     Given a correct filename fname, this program auto-formats the program 
     file. This function formats source code, in a similar fashion to    
     Python, in which "proper" matching spacing is applied for each line 
     between an opening and closing brace. 

     fname is the ONLY required argument. If fout is not defined, the
     output will have the same name as the input file except now with 
     "_edit.txt" apprended to it.

     ASUMPTIONS:
						        The file passed should have balanced braces. If this requirement is   
       not met, the program will return an Exception, unless NO_EXCEPTIONS
       is true!

       All lines of the source code can and will be "reorder" even if they
       are comments!

     ATTRIBUTES:
						        fname -- This is the name of input file.

       fout  -- This is the name of the output file. If not specificed,
         then it will be fname + "_edit.txt"

       space_count -- This is the amount of spaces, that each opening brace
         will shift the lines below it.

       special -- special arguments, see below

       NO_EXCEPTION -- Disables exceptions messages of unbalanced braces
       
      SPECIAL:
							        Treat this variable as an array of bools.  (Represented as an integer)
        This turns on/off additional functions, listed below.
        
        1 -- Comments after the end brace, what the opening brace was
        
        2 -- Use tabs, rather than spaces!

        4 -- Treat /* */ comments as braces, for the purposes of     
               indentation

        8 -- Comment-only // lines are shifted -1 left
        
        
  """
  import sys
  
  shift       = 0
  shift_delay = 0
  brace_start = '{'
									  brace_end   = '}'
	  stack       = []

  #Files 
  source_code = open(fname, "r" )
  fout = (fname + "_edit.txt") if (fout == None) else fout 
  dest_code   = open(fout, "w" )
  ###err_code    = open(fname + "_err.txt", "w" )

  print("%s starting with %s. Output is %s." % (sys._getframe(0).f_code.co_name , fname, fout) )

  for (count,line) in enumerate(source_code) :

					     ###err_code.write( '%03d | ' % len(line.strip() ) + line)

    #Empty Line are Empty
     empty_line = 1 if line.strip() else 0
   
     line = ( ( empty_line * shift * space_count * ' ' ) +
										               line.strip()                             )
		               
		     #Insert Extra Formatting here
     if special > 0:
						        if special & 1 :
														         if '{' in line and '}' not in line :
																						            stack.append( line[:-1].strip() )
         elif '{' not in line and '}' in line :
								            line += " // " + stack.pop()
       if special & 2 :
							          line = ( '\t' * shift ) + line.lstrip()
       if special & 4 :
							          if '\*' in line:
																           shift_delay +=1
         if '*\" in line:
								            shift_delay -=1
       if special & 8 :
							          if (line.lstrip()).startswith('//'):
																           if (line[0] == ' '):
																									              line = line[1:]
         
     line += '\n'

    #Write to File
     dest_code.write( line )

    ##Calculate Shift for next line
     if brace_start in line :
						        shift += 1
     if brace_end   in line :
						        shift -= 1
     if shift_delay != 0    :
						        shift += shift_delay
       shift_delay = 0
       
     if NO_EXCEPTION and shift < 0 :
						        print( "\n  File \"%s\", line %i, in %s" % ( fname, count,  sys._getframe().f_code.co_name ) )
       raise UnbalancedBraces( 0 , "Unbalanced Closing Braces in the file" )
  if NO_EXCEPTION and shift != 0:
					    print( "\n  File \"%s\" , in %s" % ( fname,  sys._getframe().f_code.co_name ) )
    raise UnbalancedBraces( 0 , "Unbalanced Opening Braces in the file!" )
  print( "%s Compeleted!" % sys._getframe(0).f_code.co_name )

def lcount( fname , fout = None, width = 6, *kargs, code = "UTF-8" ) :
				  r"""
  lcount(...)
     lcount( fname , fout = None, width = 6, *kargs, code = "UTF-8" )

     Writes the line number of each line into the output text file.

     ATTRIBUTES:
						        fname -- This is the name of input file.
       
       fout  -- This is the name of the output file. If not specificed,
         then it will be fname + "_counted.txt"
         
       width -- Sets the width of the number column
       
       code  -- Sets the default coding of the file

  """

  import sys

  #Files
  file_in  = open(fname, "r", 1, code)
  fout = (fname + '_counted.txt') if (fout == None) else fout 
  file_out = open(fout,"w" , 1, code)

  print("%s starting with %s. Output is %s." % (sys._getframe(0).f_code.co_name , fname, fout) )
    
  width = "%0" + str(width) + "d | "

  for (count,line) in enumerate(file_in) :
					    file_out.write( str( width % count) + line )  

  print( "%s Compeleted!" % sys._getframe(0).f_code.co_name )  

def rspace_killer ( fname, fout = None ) :
				  r"""
  rspace_killer(...)
     rspace_killer ( fname, fout = None )
     
     Removes excess white space on the right
     
     ATTRIBUTES:
						      
						      fname -- This is the name of the input file.
     
     fout  -- This is the name of the output file. If not specificed,
       then it will be fname + "_wk.txt"     
  """

  import sys
  
  fin = open(source,"r")
  fout = source + '_wk.txt' if ( fout == None ) else fout
  dest = open(fout,"w")

  print("%s starting with %s. Output is %s." % (sys._getframe(0).f_code.co_name , fname, fout) )
    
  for line in fin :
					    fout.write( line.rstrip() )
    
  print( "%s Compeleted!" % sys._getframe(0).f_code.co_name )  
  
if __name__ == "__main__" :
				  import sys
  print("Starting WS")
  try:
					    inf = sys.argv[1]
    outf = sys.argv[2]
    spf = sys.argv[3]
  except IndexError:
					    finput = input("Please enter a file name\n")
    fname = finput.split()
    try:
						      special = finput[1]
    except IndexError:
						      special = 0
    finally:
						      formatter(finput[0], special)
  else:
					    formatter(inf,outf, special = spf)
  pause()
  
