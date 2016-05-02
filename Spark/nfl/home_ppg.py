from pyspark import SparkContext
sc = SparkContext()

game = sc.textFile('game.csv')
header = game.first()
game.filter(lambda x: x != header)\
	.map(lambda x: x.split(','))\
	.filter(lambda x: int(x[2]) < 18)\
	.map(lambda x: (x[4], int(x[-1])))\
	.reduceByKey(lambda x, y: x + y)\
	.map(lambda x: (x[0], float(x[1]) / 128))\
	.takeOrdered(32, lambda x: -x[1])