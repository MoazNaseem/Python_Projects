#! /usr/bin/python3

import openpyxl
wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.get_sheet_by_name('Sheet')
updates = {'Garlic': 3.07, 'Celery': 1.19, 'Lemon': 1.27}
for row in range(2, sheet.max_row+1):
	produceName = sheet['A' + str(row)].value
	if produceName in updates:
		sheet['B' + str(row)] = updates[produceName]
wb.save('updatedProduceSales.xlsx')