from pyspark.sql import SparkSession

from sklearn.preprocessing import StandardScaler

from scripts.handle_file import read_file, save_file
from scripts.validate_data import validate_target_variable


spark = SparkSession.builder.appName('Preprocess data').getOrCreate()


def preprocess_data():
	df = read_file('data_batch.csv')

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

	to_drop = soil_cols + wilderness_cols + hillshade_cols

	df.drop(*to_drop)

	scaler = StandardScaler()

	save_file(spark.createDataFrame(scaler.fit_transform(df.toPandas())), 'data_batch_transformed.csv')

	else:
		raise Exception('Target column missing from dataframe.')

	return True
