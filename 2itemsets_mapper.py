#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
#ip = open("./retail/retail.dat")
for line in sys.stdin:
#for line in ip:
	# remove leading and trailing whitespace
	line = line.strip()
	# find all item ids
	transaction = re.findall(r"[\'A-Za-z0-9]+", line)
	
	# for each transaction, print all pairs of items
	for i in range(0, len(transaction)) :
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the
		# Reduce step, i.e. the input for reducer.py
		#
		# tab-delimited; the count for each 2 itemset is 1
		for j in range(i, len(transaction)-1):
			print('%s\t%s\t%s' % (transaction[i], transaction[j+1], 1))