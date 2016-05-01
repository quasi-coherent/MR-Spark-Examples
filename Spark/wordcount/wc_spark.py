import sys
import string
from pyspark import SparkContext
sc = SparkContext()

def remove_punctuation(word):
	for p in string.punctuation:
		word = word.replace(p, ' ')
	return word

txt = sc.textFile(sys.argv[1])
txt.flatMap(lambda x: x.split())\
   .map(remove_punctuation)\
   .map(lambda x: (x.strip(), 1))\
   .reduceByKey(lambda x, y: x + y)\
   .saveAsTextFile('wc-output')