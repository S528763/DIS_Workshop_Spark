from pyspark import SparkContext
logFile = "file:///C:/spark-2.3.0-bin-hadoop2.7/TestData.txt"  
sc = SparkContext("local", "first app")
logData = sc.textFile(logFile).cache()
num = logData.count()
print "=========================================="
print "Line Count is : %i" % (num)