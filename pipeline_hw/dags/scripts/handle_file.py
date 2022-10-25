import os
from pyspark.sql import SparkSession

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = '/data/'

spark = SparkSession.builder.appName('Handling CSV files').getOrCreate()


def read_file(file_name):
	df = spark.read.format('csv').load(DATA_DIR, file_name)
	return file_name

def save_file(df, file_name):
	df.write.csv(os.path.join(DATA_DIR, file_name))

def delete_file(file_name):
	if os.path.exists(DATA_DIR, file_name):
		os.remove(os.path.join(DATA_DIR,file_name))