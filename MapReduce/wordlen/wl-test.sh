#!/usr/bin/env bash
cat wl_input.txt | ./wl_map1.py | sort | ./wl_reduce.py | \
./wl_map2.py | sort | ./wl_reduce.py