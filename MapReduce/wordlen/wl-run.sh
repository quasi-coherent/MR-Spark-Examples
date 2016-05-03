#!/usr/bin/env bash
hadoop fs -put wl_input.txt
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files wl_map1.py,wl_reduce.py \
  -input wl_input.txt \
  -output wl_output0 \
  -mapper wl_map1.py \
  -reducer wl_reduce.py
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files wl_map2.py,wl_reduce.py \
  -input wl_output0 \
  -output wl_output \
  -mapper wl_map2.py \
  -reducer wl_reduce.py 
hadoop fs -get wl_output/part-00000
hadoop fs -rm -r wl_output0 wl_output
hadoop fs -rm wl_input.txt
mv part-00000 wl_output.txt