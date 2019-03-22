#! /usr/bin/python3

import os, zipfile, shutil

def selective(folder, distination):
	# Get the absolute path of the folders
	folder = os.path.abspath(folder)
	dis = os.path.abspath(distination)
	disPdf = '/home/mizo/Documents/PythonProjects/selective/pdfFiles'
	disPy = '/home/mizo/Documents/PythonProjects/selective/PythonFiles'
	pdfBase = os.path.basename(disPdf)
	pyBase = os.path.basename(disPy)
	# Figure out a ZIP file's name.
	number = 1
	while True:
		zipFileName = os.path.basename(distination) + '_' + str(number) + '.zip'
		# If the file with that numbe doesn't exist, then good, get out of the loop, in case it exists, try the next number.
		if not os.path.exists(zipFileName):
			break
		number += 1
	# Creating the actual ZIP file
	print('Creating %s...' %(zipFileName))
	backupZip = zipfile.ZipFile(zipFileName, 'w')

	# Walking through the folder tree.
	for foldername, subfolders, filenames in os.walk(folder):
		# searching for files ends with .pdf or .py
		for filename in filenames:
			if filename.endswith('.pdf'):
				if os.path.exists(os.path.join(disPdf, filename)):
					break
				shutil.move(os.path.join(foldername ,filename), disPdf)
			elif filename.endswith('.py'):
				if os.path.exists(os.path.join(disPy, filename)):
					break
				shutil.move(os.path.join(foldername ,filename), disPy)
	backupZip.write(disPdf, compress_type=zipfile.ZIP_DEFLATED)
	backupZip.write(disPy, compress_type=zipfile.ZIP_DEFLATED)
	for foldername, subfolders, filenames in os.walk(dis):
		# Back the current folder
		print('Backing %s...' %(foldername))
		backupZip.write(foldername, compress_type = zipfile.ZIP_DEFLATED)
		for filename in filenames:
			backupZip.write(os.path.join(foldername, filename), compress_type=zipfile.ZIP_DEFLATED)
	backupZip.close()
	print('Done.')

selective('./textfiles', './selective')

