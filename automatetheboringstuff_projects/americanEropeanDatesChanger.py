#! /usr/bin/python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY and the other way around.

import re
import shutil
import os


def rename_file(europeanName, match):
    # Get the full, absolute file paths.
    currentPath = os.path.abspath('.')
    fileName = os.path.join(currentPath, match[1])
    europeanName = os.path.join(currentPath, europeanName)

    # Rename the files.
    shutil.move(fileName, europeanName)


def form_new_date(beforePart, monthPart, dayPart, yearPart, afterPart, match):
    print(f'day: {dayPart}, month: {monthPart}')
    # Form the European-style filename.
    europeanName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    rename_file(europeanName, match)


def breakdown_old_date(matches):
    for match in matches:
        # Get the different parts of the filename.
        beforePart = match[0].group(1)
        monthPart = match[0].group(2)
        dayPart = match[0].group(4)
        yearPart = match[0].group(6)
        afterPart = match[0].group(8)
        form_new_date(beforePart, monthPart, dayPart, yearPart, afterPart, match)


def search_files(dataPattern):
    matches = []
    # Loop over the files in the working directory.
    for fileName in os.listdir('.'):
        matchObj = dataPattern.search(fileName)
        # Skip files without a date.
        if not matchObj:
            continue
        else:
            matches.append((matchObj, fileName))
    breakdown_old_date(matches)


def form_regex():
    # Create a regex that can identify the text pattern of American-style dates.
    dataPattern = re.compile(r"""
        ^(.*?)                              # all text before the date
        ((0|1|2|3)?\d)-                         # one or two digits for the month
        ((0|1|2|3)?\d)-                     # one or two digits for the day
        ((19|20)\d\d)                       # four digits for the year
        (.*?)$                              # all text after the date
        """, re.VERBOSE)
    search_files(dataPattern)


if __name__ == "__main__":
    form_regex()
