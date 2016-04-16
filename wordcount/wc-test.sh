#!/usr/bin/env bash
cat wc_input.txt | ./wc_map.py | sort | ./wc_reduce.py >! wc_output.txt
