package wordcount

import org.apache.spark.{SparkConf, SparkContext}

object WordCount {
  def main(args: Array[String]) = {
    val conf = new SparkConf()
        .setAppName("Wordcount")
        .setMaster("yarn-client")

    val sc = new SparkContext(conf)
    val file = args(0)

    val wc = sc.textFile(file)
        .flatMap(_.split(" "))
        .map(word => (word.toLowerCase().replaceAll("[^a-zA-Z]", ""), 1))
        .filter(_._1.nonEmpty)
        .reduceByKey(_ + _)
        .sortBy(_._2, ascending = false)

    wc.saveAsTextFile("wc-output")
    sc.stop()
  }
}
