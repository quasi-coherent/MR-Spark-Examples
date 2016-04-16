#!/usr/bin/env python
import sys


for line in sys.stdin:
	lis = line.split('\t')
	team = lis[16]
	player = lis[0]
	avg = float(lis[2]) / float(lis[1])
	print('%s\t%s,%s' % (team, player, avg))