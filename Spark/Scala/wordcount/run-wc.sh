spark-submit --class wordcount.WordCount \
target/scala-2.11/wordcount_2.11-1.0.jar \
trump_speeches.txt
hdfs dfs -getmerge wc-output wc-output.txt 
