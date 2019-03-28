#! /usr/bin/python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):

	# Backup the entire contents of "folder" into a ZIP file.
	folder = os.path.abspath(folder)		# make sure the folder is absolute
	
	# Figure out the ZIP file's name.
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number += 1
	# Creating the actual ZIP file
	print('Creating %s' %(zipFilename))
	backupZip = zipfile.ZipFile(zipFilename, 'w')

	# Walking through the folder tree and backing every file.
	for foldername, subfolders, filenames in os.walk(folder):

		# Back the current folder.
		print('Backing up %s...' %(foldername))
		backupZip.write(foldername, compress_type=zipfile.ZIP_DEFLATED)

		for filename in filenames:
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and endswith('.zip'):
				continue
			backupZip.write(os.path.join(foldername, filename), compress_type=zipfile.ZIP_DEFLATED)
	backupZip.close()
	print('Done.')

backupToZip('./textfiles')
