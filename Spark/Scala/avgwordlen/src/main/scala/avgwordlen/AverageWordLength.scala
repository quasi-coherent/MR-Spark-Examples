package avgwordlen

import org.apache.spark.{SparkConf, SparkContext}

object AverageWordLength {
  def main(args: Array[String]) = {
    val conf = new SparkConf()
        .setAppName("Average Word Length")
        .setMaster("yarn-client")

    val sc = new SparkContext(conf)
    val file = args(0)

    val totals = sc.textFile(file)
        .flatMap(_.split(" "))
        .map(word => (word.toLowerCase().replaceAll("[^a-zA-Z]", "").length, 1))
        .reduce((x, y) => (x._1 + y._1, x._2 + y._2))

    println("Average word length: " + totals._1.toFloat / totals._2)

  }

}
