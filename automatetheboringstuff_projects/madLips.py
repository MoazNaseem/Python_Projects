#! /usr/bin/python3

import re

spam = 'The ADJECTIVE panda walked to the NOUN and then VERB A nearby NOUN was unaffected by these events.'
print(spam)
spamList = spam.split()
print(spamList)

nvaRegex = re.compile(r'NOUN|VERB|ADJECTIVE')
nvaList = nvaRegex.findall(spam)
print(nvaList)
for item in range(len(nvaList)):
	if nvaList[item] == 'ADJECTIVE':
		print('Enter an adjective:')
		nvaList[item] = input()
	elif nvaList[item] == 'NOUN':
		print('Enter a noun:')
		nvaList[item] = input()
	elif nvaList[item] == 'VERB':
		print('Enter a verb:')
		nvaList[item] = input()
print(nvaList)

for i in range(len(spamList)):
	j = 0
	if spamList[i] == 'ADJECTIVE':
		spamList[i] = nvaList[j]
		j += 1
	elif spamList[i] == 'NOUN':
		spamList[i] = nvaList[j]
		j += 1
	elif spamList[i] == 'VERB':
		spamList[i] = nvaList[j]
		j += 1

spam = ' '.join(spamList)		
print(spam)