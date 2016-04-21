import sys, string
from pyspark import SparkConf, SparkContext


def remove_punctuation(text):
	for p in string.punctuation:
		text = text.replace(p, ' ')
	return text

sc = SparkContext(AppName="wordcount")

sc.textFile(sys.argv[1])\
	.map(lambda x: remove_punctuation(x.lower()))\
	.flatMap(lambda x: x.split())\
	.map(lambda x: (x, 1))\
	.reduceByKey(lambda x, y: x + y)\
	.saveAsTextFile(sys.argv[2])