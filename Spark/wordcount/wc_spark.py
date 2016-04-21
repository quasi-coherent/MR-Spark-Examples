import sys, string
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("wordcount")
sc = SparkContext(conf=conf)
script, input_file, output_file = sys.argv


def remove_punctuation(text):
	for p in string.punctuation:
		text = text.replace(p, ' ')
	return text

sc.textFile(input_file)\
	.map(lambda x: remove_punctuation(x.lower()))\
	.flatMap(lambda x: (x, 1))\
	.reduceByKey(lambda x,y: x+y)\
	.saveAsTextFile(output_file)