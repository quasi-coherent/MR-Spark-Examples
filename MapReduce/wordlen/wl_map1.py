#!/usr/bin/env python
import sys
import string


for line in sys.stdin:
	for p in string.punctuation:
		line = line.replace(p, ' ')
	words = map(lambda x: x.lower(), line.split())
	for word in words:
		print '%s\t1' % word