#!/usr/bin/env python
import sys


word = None
count = 0

for line in sys.stdin:
	record = line.split('\t')
	next_word = record[0]
	value = int(record[1])
	if next_word == word:
		count += value
	else:
		if word is None:
			word = next_word
			count = value
		print '%s, %d' % (word, count)
		word = next_word
		count = value
print '%s, %d' % (word, count)