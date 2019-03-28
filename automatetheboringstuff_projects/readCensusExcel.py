#! /usr/bin/python3
# readCensusExcel.py - Tabulates population and number of census
# tracts for each county.

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}
for row in range(2, sheet.max_row+1):
	state = sheet['B' + str(row)].value
	county = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value
	print(row, state, county, pop)
	# Make sure the key for this state exists.
	countyData.setdefault(state, {})
	# Make sure the key for this county exists.
	countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
	# Add the values to the dictionary.
	countyData[state][county]['tracts'] += 1
	countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it.
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
