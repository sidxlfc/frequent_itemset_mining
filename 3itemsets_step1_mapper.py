#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	#split line on tabs
	line = line.split("\t")
	# print these items
	print('%s\t%s' % (line[0], line[1]))
		#break
	#break