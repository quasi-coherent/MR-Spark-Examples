#!/usr/bin/env bash
hadoop fs -put ba_input.csv
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files ba_map.py,ba_reduce.py \
  -input ba_input.csv \
  -output ba_output \
  -mapper ba_map.py \
  -reducer ba_reduce.py
hadoop fs -get ba_output/part-00000
hadoop fs -rm -r ba_output
hadoop fs -rm ba_input.csv
mv part-00000 ba_output.txt
