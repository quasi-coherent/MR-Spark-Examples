#!/usr/bin/env python
import sys

team = None
best_player = None
max_avg = 0
for line in sys.stdin:
	next_team, value = line.split('\t')
	player = value.split(',')[0]
	avg = float(value.split(',')[1])
	if next_team == team:
		if avg > max_avg:
			best_player = player
			max_avg = avg
	elif team is None:
		team = next_team
		best_player = player
		max_avg = avg
	else:
		print('%s: %s, %s' % (team, best_player, max_avg))
		team = next_team
		best_player = player
		max_avg = avg
print('%s: %s, %s' % (team, best_player, max_avg))