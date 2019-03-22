#! /usr/bin/python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword. 	leng(argv) == 3
#py.exe mcb.pyw delete <keyword> - delete keyword from the shelf.		leng(argv) == 3
#py.exe mcb.pyw <keyword> - Loads keyword to clipboard.					leng(argv) == 2
#py.exe mcb.pyw list - Loads all keywords to clipboard.					leng(argv) == 2
#py.exe mcb.pyw delete - delete all keywords.							leng(argv) == 2

import sys, pyperclip, shelve

mcbShelf = shelve.open('mcb')
# Save clipboard content.
if len(sys.argv) == 3:
	if sys.argv[1].lower() == 'save':
		# save clipboard to keyword, it's like saving to a dictionary.
		mcbShelf[sys.argv[2]] = pyperclip.paste()

		# delete keyword from the shelf.
	if sys.argv[1].lower() == 'delete':
		del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
	# if list, return all the keys to the clipboard.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))

	# if delete, delete all the keys from the shelf.
	elif sys.argv[1].lower() == 'delete':
		for key in mcbShelf.keys():
			mcbShelf.pop(key)

	# if keyword, return the keyword to the clipboard.
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
