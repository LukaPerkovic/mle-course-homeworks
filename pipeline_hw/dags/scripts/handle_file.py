import findspark
findspark.init()

import os
import logging
import pandas as pd
from pyspark.sql import SparkSession

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = '/opt/airflow/data/'

spark = SparkSession.builder.appName('Handling CSV files').getOrCreate()

def read_file(file_name):
	PATH = os.path.join(DATA_DIR, file_name)
	df = spark.read.csv(PATH, header='true')
	# df = pd.read_csv(PATH)
	return df.toPandas()

def save_file(df, file_name):
	PATH = os.path.join(DATA_DIR, file_name)
	delete_file(file_name)
	# df.write.csv(os.path.join(DATA_DIR, file_name))
	df.to_csv(PATH)

def delete_file(file_name):
	PATH = os.path.join(DATA_DIR, file_name)
	if os.path.exists(PATH):
		os.remove(PATH)