#!/usr/bin/env python

import sys

# initialize an empty candidates array
candidates = []

# read the candidates file and put it into a proper format
def make_candidates():
	
	temp = []

	for candidate in open("candidates") :

		candidate = candidate.strip()
		candidate = candidate.split("\t")
		temp.append((int(candidate[0]), int(candidate[1]), int(candidate[2])))

	candidates = temp

make_candidates()
# input comes from STDIN (standard input)
for line in sys.stdin:
	
	# remove leading and trailing whitespace
	line = line.strip()
	line = line.split(" ")

	# make sure everything in the transaction array is in int format
	transaction = [int(line[i]) for i in range(0, len(line))]

	for candidate in candidates :

		#let's assume this transaction contains
		#all items
		count = 0

		for item in candidate :

			if item not in transaction :
				# if any of the items is absent from the transaction,
				# no need to check further
				#flag = True
				break

			count += 1

		#print only if all items are contained in this transaction
		if count >= 3 :
			print('%s\t%s\t%s\t%s' % (candidate[0], candidate[1], candidate[2], 1))