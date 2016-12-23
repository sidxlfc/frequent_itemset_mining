#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)

for line in sys.stdin:

	# remove leading and trailing whitespace
	line = line.strip()
	line = line.split("\t")

	# print data as per the incoming frequent k-itemset, where k = 1,2
	if len(line) == 2:

		line = (int(line[0]), int(line[1]))
		#line = sorted(line)
		print('%s\t%s' % (line[0], line[1]))
		
	elif len(line) == 3 :

		line = (int(line[0]), int(line[1]), int(line[2]))
		
		print('%s\t%s\t%s' % (line[0], line[1], line[2]))