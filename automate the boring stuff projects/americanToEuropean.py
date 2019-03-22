#! /usr/bin/python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import re, shutil, os

#Create a regex that can identify the text pattern of American-style dates.
dataPattern = re.compile(r"""
	^(.*?)								# all text before the date
	((0|1)?\d)-							# one or two digits for the month
	((0|1|2|3)?\d)-						# one or two digits for the day
	((19|20)\d\d)						# four digits for the year
	(.*?)$								# all text after the date
	""", re.VERBOSE)

# TODO: Loop over the files in the working directory.
for fileName in os.listdir('.'):
	mo = dataPattern.search(fileName)

	# TODO: Skip files without a date.
	if mo == None:
		continue

	# TODO: Get the different parts of the filename.
	beforePart 	= 	mo.group(1)
	monthPart 	= 	mo.group(2)
	dayPart 	= 	mo.group(4)
	yearPart 	= 	mo.group(6)
	afterPart 	= 	mo.group(8)


	# TODO: Form the European-style filename.
	europeanName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart


	# TODO: Get the full, absolute file paths.	
	cwPath = os.path.abspath('.')
	fileName = os.path.join(cwPath, fileName)
	europeanName =  os.path.join(cwPath, europeanName)

	# TODO: Rename the files.
	shutil.move(fileName, europeanName)
