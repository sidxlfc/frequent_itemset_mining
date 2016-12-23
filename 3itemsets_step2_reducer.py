#!/usr/bin/env python

import sys

current_word = None
word = None

# initialize a temporary array and an empty dictionary
temp = []
d = {}

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	line = line.split('\t')

	# if this is a frequent 2-itemset, 
	# put the first item in the second item's dictionary,
	# and vice versa
	if len(line) == 2 :

		line = (int(line[0]), int(line[1]))

 		if line[0] in d :

 			d[line[0]][line[1]] = 1

 		else :

 			d[line[0]] = {}
 			d[line[0]][line[1]] = 1

 		if line[1] in d :

 			d[line[1]][line[0]] = 1

 		else :

 			d[line[1]] = {}
 			d[line[1]][line[0]] = 1

 	# if this is a 3-itemset, just put it in the temp array
 	elif len(line) == 3 :

 		line = (int(line[0]), int(line[1]), int(line[2]))
 		temp.append(line)

# after all input has been received,
# see if for each 3-itemset in the temp array,
# one item contains the other 2 in its dictionary.
# if not, then don't print
for transaction in temp :

	if transaction[1] not in d[transaction[0]] or transaction[2] not in d[transaction[0]] :
		continue

	if transaction[0] not in d[transaction[1]] or transaction[2] not in d[transaction[1]] :
		continue

	if transaction[0] not in d[transaction[2]] or transaction[1] not in d[transaction[2]] :
		continue
	
	print('%s\t%s\t%s' % (transaction[0], transaction[1], transaction[2]))