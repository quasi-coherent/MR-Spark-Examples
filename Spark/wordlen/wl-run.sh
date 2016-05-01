#!/usr/bin/env bash
hadoop fs -put ~/Github/MR-Spark-Examples/MapReduce/wordcount/wc_input.txt
$SPARK_HOME/bin/spark-submit ~/Github/MR-Spark-Examples/Spark/wordlen/wl_spark.py wc_input.txt
hadoop fs -get wl-output
hadoop fs -rm -r wl-output