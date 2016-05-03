#!/usr/bin/env python
import sys

for line in sys.stdin:
	word = line.split(',')[0]
	print '%s\t1' % len(word)