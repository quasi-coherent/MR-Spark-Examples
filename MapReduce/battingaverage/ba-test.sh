#!/usr/bin/env bash
cat ba_input.csv | ./ba_map.py | sort | ./ba_reduce.py
