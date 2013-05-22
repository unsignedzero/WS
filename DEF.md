---------------------------------------------------------------

 - Table of Contents
 - - Use Ctrl/Cmd + F to jump to certain part of this text
 - - using the characters between the [ and ].

 -  (0*) Information
 - - 00 [Adin] Additional Information
 - - 01 [DEBG] Debug Information

 -  (A*) Functions 
 - - A0 [PASE] pause
 - - A1 [FMAT] formatter
 - - A2 [LCUT] lCount
 - - A3 [RiSK] rSpace_siller

 -  (E*) Exceptions
 - - E0 [PASE] ZText_Error
 - - E1 [FMAT] UnbalancedBraces

 -  (S*) Script
 - - S0 [MAIN] __main__

 -  (Z*) End Information
 - - Z0 [ABUT] About 

---------------------------------------------------------------
---------------------------------------------------------------
 -  (0*) Information
---------------------------------------------------------------
 - - 00 [Adin] Additional Information

There are two versions of this Python Script. Remember to use 
the right version.

As with other Python Scripts, this can be imported but also ran
directly from the script. When executed directly, this script 
will use the formatter function. 

If arguments are passed, the first argument will be the input, 
the second argument will be the output file and the third will
be a bool flag array, in the form of an integer. If the third 
argument is not passed, no special formatting will be used.
If the second argument is not pass, then the output will be 
the input file name with "_edit.txt" concatenated on the end
of it. 

If no arguments as passed, then a prompt will run in 
the script, asking for the above info. 

For more information on the flag parameters see the actual 
function formatter or the docstring of formatter.

---------------------------------------------------------------
 - - 01 [DEBG] Debug Information

Certain functions within this module have debugging functions.

EXCEPTION is a keyword that can be passed to TURN OFF PRESET 
exceptions within that function. (Note: Exceptions due to bad 
input will still occur!)

debug is a keyword that can be passed to on debug mode, for
the function. (Currently this does nothing.)

---------------------------------------------------------------
 -  (A*) Functions 
---------------------------------------------------------------
- - A0 [PASE] pause ()

Function:
WS.pause
()

This function mimics ZX::ZOS(2) without relying on the OS. 
This function pauses the executing module and waits for the 
user to hit the enter key. Anything, entered is discarded.

-PreCondition:
None.

-PostCondition:
The program is pause once before execution resumes.

---------------------------------------------------------------
 - - A1 [FMAT] formatter (String, ...)

Function:
WS.formatter
( fname, fout = None, space_count = 2, *kargs, special = 0, 
  EXCEPTION = False )

This is the core of WS. Minimally, fname (string) the 
name of the input file must be passed. Additional formatting
and information can be passed as well. 

This function assumes that the code passed is has mostly* 
proper syntax and is curly brace balanced! This function 
ONLY works on languages that use curly braces. Languages 
such as Python will NOT format properly because there is
no way to tell if a line is in the right scope of the
right conditional expression.

In addition, this code DOES check for balanced curly 
braces. Should you be passing a file that might not be,
set EXCEPTION to be false and special & 1 to be true, 
for your own debugging purposes

fout -- This the name of the output file. By default, if 
None is passed, this will be set to the fname + "_edit.txt".

space_count -- This is the number of space/tab used for an 
indent. Values should be above 0.

special -- This is a formatting flag for the formatter 
function. Treat this as a bool array that is stored in an 
integer. The result integer passed will be bitwise anded
with the numbers below to turn on/off additional 
functionality. By default this is 0 (Nothing extra).

  1 -- For all closing braces, '}' the condition of the 
    matching opening brace will be shown to the right of the
    closing brace that the formatter is currently scanning, 
    but commented so as not to effect the code. 
    
    Useful for debugging purposes and trying to pair up
    the right curly braces.

  2 -- The tab character will replace the space character that
    is used for indenting. Please note that the space_count 
    will tell formatter how many tabs to place.

    For the purposes of the documentation of this function, 
    spaces and tabs can be used interchangeably depending on
    this flag ONLY. That is, if a function talks about 
    indenting two spaces and this flag is set, the function
    will not indent with two tab characters.

  4 -- Block comments will also be intended, treated as 
    opening and closing braces.

  8 -- Comment lines are shifted back one, so they stand out.
    Will only work if the comment has spaces/tabs to the left.

 16 -- Non-braced if/else/for/while will indent
    This is currently being developed and this flag is in beta

EXCEPTION -- This flag disable balanced curly brace 
exceptions in this function. ALL OTHER EXCEPTIONS will still 
occur! Use carefully of test code with 1 to see which 
braces match with which conditional expression.

-PreCondition:
A valid source code file, that has mostly* correct source 
code. Additional, information can be passed.

-PostCondition:
A properly "formatted" source code file.

!WARNING:Sending invalid or other non-source code files 
will most likely result in erroneous formatting and even
exceptions. In the rare case that it should work out, the
file is curly brace balanced!

*I say mostly because most typos, programmer make will have 
little to no effect on formatter. Formatter checks mainly
for braces and the keywords if/else/for/while and unless 
these are place incorrectly or misspelled, formmater should
have no problems. That being said your mileage will vary.

---------------------------------------------------------------
 - - A2 [LCUT] lcount (String, ...)

Function:
WS.lcount
( fname , fout = None, width = 6, *kargs, code = "UTF-8" )

This function simply takes the input file and writes it to 
the output file, in addition to the line numbers. Line count
starts at 1.

fname -- This is the name of the input file. Unlike formatter,
this function will run regardless of the what the file is. 
However, in the case that the file passed in not a source code,
the length of the line CAN very drastically.

fout -- This is the name of the output file. By default, if 
None is passed then name will be fname + '_counted.txt'

width -- This is the number of additional chars that will be 
added to the beginning of each line for the line count. This 
space will be used for placing the line number. By default 
this is set to 6. 

code -- This sets the character set which will
determine how this function will interpret the input file.
By default this is UTF-8. 

-PreCondition:
A valid file.

-PostCondition:
The output file with line numbers.

---------------------------------------------------------------
 - - A3 [RiSK] rspace_killer (String, ...)

Function:
WS.rspace_killer
( fname, fout = None )

This function removes the pesky whitespace at the end of each
line. While this may seem trivial, the white space does add up.

fname -- The input source code file. If this is NOT a code file,
unexpected results may be created.

fout -- The name of the output file. By default, this function 
will return fname + "_wk.txt" 

-PreCondition:
A valid source code file is passed.

-PostCondition:
The whitespace at the end of each line is removed.
---------------------------------------------------------------
 -  (E*) Exceptions
---------------------------------------------------------------
 - - E0 [PASE] ZText_Error ( Exception )

Exception:
class WS.ZText_Error
( Exception )

This is the base exception class for this module. This 
exception itself is never called but is inherited by other 
exceptions.

---------------------------------------------------------------
 - - E1 [FMAT] UnbalancedBraces ( ZText_Error )

Exception:
class WS.UnbalancedBraces
( ZText_Error )

This is the UnbalancedBrace Exception that is called in
formatter when there is an Unbalanced Curly Brace in the 
source code that formatter is analyzing. 

---------------------------------------------------------------
 -  (S*) Script
---------------------------------------------------------------
 - - S0 [MAIN] __main__

Script Execution:
WS.__main__

This is the script of WS that is executed when this code is 
ran directly, not imported.

This code itself will take in inputs but also created a mini
prompt if none are given. This script itself will run the 
formatter function in WS with standard input , output and  
flags. For more specialized purposes, edit the source code!

Regardless of how the arguments are acquired, via prompt, or
via the shell executing WS, the input is parsed the same way.

If there arguments as passed, then the first argument is the 
input file, the second argument is the output file and the
third is the argument flags for formatter.

if the third argument is omitted then the all the flags will 
be set to 0. If the third AND second argument are omitted, 
then formatter will write to the default output, which is the
input file name with "_edited.txt" concatenated at the end.

Should all there arguments be missing then the mini prompt 
is executed excepting at least one input. The one to three 
inputs given will be treated and parsed the same way, as if 
they were passed in from the shell.

---------------------------------------------------------------

---------------------------------------------------------------
 -  (Z*) End Information
---------------------------------------------------------------
 - - Z0 [ABUT] About 

This program was originally created by unsignedzero to format 
garbage C++ code. Now it can format any code language so long 
as it uses curly braces.

Original Project Name:WonderSwan
Started:July 04, 2011 
Created by unsignedzero
Built in Python V3.2 (NO IDE) Unicode

For more information see 
https://bitbucket.org/unsignedzero/ws/overview
You may contact me via email (unsignedzero@gmail.com) if you
have any suggestions and comments. I DON'T check it daily.

---------------------------------------------------------------
---------------------------------------------------------------
|  -- END OF FILE --   -- END OF FILE --   -- END OF FILE --  |
---------------------------------------------------------------
