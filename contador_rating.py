from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)
lines = sc.textFile("file:///CursoSpark/ml-100k/u.data")

# Acciones
lines.first()

for line in lines.take(5):

    print(line)

print(lines.count())

# Transformaciones
lines.filter()
#=======================================
rating = lines.map(lambda x: x.split()[2])
result = rating.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key,value))
