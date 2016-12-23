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

	word = (int(temp[0]), int(temp[1]), int(temp[2]))
	word = sorted(word)
	count = temp[3]

	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	if current_word == word:
		current_count += count
	else:
		if current_word and current_count >= 1000:
			# write result to STDOUT
			print('%s\t%s\t%s' % (current_word[0], current_word[1], current_word[2]))
		current_count = count
		current_word = word

if current_word == word and current_count>1000:
	print('%s\t%s\t%s' % (current_word[0], current_word[1], current_word[2]))