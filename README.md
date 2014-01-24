# WhiteSpace #

Abstract:
The purpose of this code is to provide a set of functions for formatting,
debugging and related purposes for programmers.
As with other Python Scripts, this can be executed directly.
In this case, it will run the formatter function or formatter and lcount if
debug is set.

I assume that this script will be used on systems with at Python version 2.5 or
greater. Version 2.5 was selected because that was when the ternary operator was
added.

Created by David Tran (unsignedzero)

# TO DO #

* Parse DEF.md and update with markdown syntax
* Special 16 has a few bugs to iron out.

# Version/Changelog #

* .gitignore file updated.
* Cleaning up README.md.
* Updated DEFinitions file to markdown format

## Version 0.9.0.0 05-21-2013 #
* Updated old code repo to
  * Use Markdown for README
  * Use ArgsParse rather than manually parse input
  * Cleaned up string concat to use % operator rather than +
* Batch mode can take any amount of arguments for files.
* Debug option added so it spits the file with line count and matching
  conditionals
* Works with JS files
* Changed to MIT license
* Merged README, history and notice into this file (README.md)

## Version 0.8.3.1 11-29-2011 #
* Edited comments and readme for grammatical errors and miscellaneous mistakes.
* EXCEPTION in v3 is default true, like v2.5
* Debug flag created.
* \*Will update 16 and add debug soon.

## Version 0.8.3.0 11-01-2011 #
* \*The updated code from 0.8.1.0 will work from v2.5 and onward, not v2 due
  to the use of the ternary operator.
* README created.
* Additional comments placed in the code.
* Default value for the output file can be set by passing 0.
* \*Will update 16 and add debug soon.

## Version 0.8.2.1 10-31-2011 #
* Added additional comments to code.
* \*Will update 16 and add debug soon.
* Grammar fixed on all files.

## Version 0.8.2.0 10-25-2011 #
* Fixed bad input to the script
* Included .sh script to run the code manually
* Calling the script will automatically run if there are 1 or 2 arguments passed.
* Added new mode (16) to formatter
* All lines in code are 80 characters or less

## Version 0.8.1.0 10-18-2011 #
* Bugs fixed.
* Two versions of code, one for v2 python and one for v3 python.
* Codes both work and annoying split bug is also fixed.

## Version 0.8.0.1 10-18-2011 #
* Fixed funky format on GIT

## Version 0.8.0.0 10-09-2011 Raiser #
* All code now in one file.
* Exceptions added and additional modes added.
* No module docstrings have been made YET but all functions have docstrings

## Version 0.5.0.0 07-24-2011 Foundation #
* Original Work Code Created.
* All functions in separate files
