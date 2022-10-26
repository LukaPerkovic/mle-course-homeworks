import pyspark
from pyspark.sql

spark = SparkSession.builder.appName('Dataset Validation').getOrCreate()

def validate_target_variable(df, type, target_variable:str):
	if type == 'train' and target_variable in df.columns:
		return True
	elif type == 'test' and target_variable not in df.columns:
		return True
	else:
		False
