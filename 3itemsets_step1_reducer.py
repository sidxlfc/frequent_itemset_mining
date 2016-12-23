#!/usr/bin/env python

import sys

current_word = None
current_count = 0
word = None

#initialize an empty dictionary
d = {}

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	temp = line.split('\t')

	# put the items in a tuple,
	# and assign that tuple to a word
	word = (temp[0], temp[1])
	#sorted(word)
	
	# this IF-switch only works because Hadoop sorts map output
	# by key (here: 2 itemset) before it is passed to the reducer
	if current_word :

		#check if this item is the dictoinary d
		if current_word[0] in d :

			# for each frequent item associated with this item,
			# print th 3 itemset formed by the items produced by map
			# and the item contained in this dictionary
			for item in d[current_word[0]] :
				# write result to STDOUT
				print('%s\t%s\t%s' % (current_word[0], current_word[1], item))

			# put this item in the dictionary of current word[0]
			# i.e., the first item
			d[current_word[0]][current_word[1]] = current_count

		#if not present, initialize an empty dictionary for this item,
		# and add a new item (current_word[1]) for it
		else :

			d[current_word[0]] = {}
			d[current_word[0]][current_word[1]] = current_count

		# Do the same for the second item, current_word[1]
		if current_word[1] in d :

			for item in d[current_word[1]] :
				# write result to STDOUT
				print('%s\t%s\t%s' % (current_word[0], current_word[1], item))

		else :

			d[current_word[1]] = {}

	current_word = word

# print for the last itemset
if current_word == word:

	if current_word[0] in d :

		for item in d[current_word[0]] :
			# write result to STDOUT
			print('%s\t%s\t%s' % (current_word[0], current_word[1], item))

		d[current_word[0]][current_word[1]] = current_count

	else :

		d[current_word[0]] = {}
		d[current_word[0]][current_word[1]] = current_count

	if current_word[1] in d :

		for item in d[current_word[1]] :
			# write result to STDOUT
			print('%s\t%s\t%s' % (current_word[0], current_word[1], item))

	else :

		d[current_word[1]] = {}