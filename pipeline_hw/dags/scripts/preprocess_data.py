# import findspark
# findspark.init()
import logging
import pandas as pd
# from pyspark.sql import SparkSession

from sklearn.preprocessing import StandardScaler

from scripts.handle_file import read_file, save_file
from scripts.validate_data import validate_target_variable


# spark = SparkSession.builder.appName('Preprocess data').getOrCreate()


def preprocess_data():
	df = read_file('data_batch.csv')
	logging.warn(f'Dataset info: {df.shape}--{df.columns}')
	if validate_target_variable(df, 'train', target_variable='Cover_Type'):

		soil_cols = [name for name in df.columns if name.startswith("Soil")]
		wilderness_cols = [name for name in df.columns if name.startswith("Wild")]
		hillshade_cols = [name for name in df.columns if name.startswith("Hill")]
		restof_columns = [
			"Elevation",
			"Aspect",
			"Slope",
			"Horizontal_Distance_To_Hydrology",
			"Vertical_Distance_To_Hydrology",
			"Horizontal_Distance_To_Roadways",
		]

		to_drop = soil_cols + wilderness_cols + hillshade_cols + ['Horizontal_Distance_To_Fire_Points']

		# df = df.drop(*to_drop)

		df = df.drop(to_drop, axis=1)
		

		X = df.drop('Cover_Type', axis=1)
		X_col_names = X.columns

		y = df.Cover_Type

		scaler = StandardScaler()

		df = pd.DataFrame(data=scaler.fit_transform(X), columns=X_col_names)

		df['Cover_Type'] = y

		# save_file(spark.createDataFrame(scaler.fit_transform(df.toPandas())), 'data_batch_transformed.csv')
		save_file(df, 'data_batch_transformed.csv')

	else:
		raise Exception('Target column missing from dataframe.')

	return True
