#!/usr/bin/env bash
hadoop fs -put wc_input.txt
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files wc_map.py,wc_reduce.py \
  -input wc_input.txt \
  -output wc_output \
  -mapper wc_map.py \
  -reducer wc_reduce.py
hadoop fs -get wc_output/part-00000
hadoop fs -rm -r wc_output
hadoop fs -rm wc_input.txt
mv part-00000 wc_output.txt
