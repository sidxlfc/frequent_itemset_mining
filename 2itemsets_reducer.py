#!/usr/bin/env python

import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	temp = line.split('\t')

	#the first 2 items in temp are the item ids
	word = (temp[0], temp[1])
	sorted(word)

	# the third value is the count
	count = temp[2]

	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: 2 itemset) before it is passed to the reducer
	if current_word == word:
		current_count += count
	else:

		#print only if this 2 itemset is frequent
		if current_word and int(current_count) > 1000:
			# write result to STDOUT
			print('%s\t%s' % (current_word))
		current_count = count
		current_word = word

# do not forget to output the last 2 itemset if needed!
if current_word == word and current_count>1000:
	print('%s\t%s' % (current_word))