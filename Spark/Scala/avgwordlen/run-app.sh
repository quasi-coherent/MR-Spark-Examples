hdfs dfs -put trump_speeches.txt
spark-submit --class avgwordlen.AverageWordLength \
target/scala-2.11/avgwordlen_2.11-1.0.jar \
trump_speeches.txt
# Average word length: 3.957392
