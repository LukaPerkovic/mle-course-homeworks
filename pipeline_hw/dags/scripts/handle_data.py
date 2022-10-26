import pandas as pd


from sqlalchemy import create_engine

from scripts.handle_file import load_file
import utils.ml_pipeline_config as config


db_engine = config.params['db_engine']
db_schema = config.params['db_schema']
batch_table = config.params['data_batch_table']


spark = SparkSession.builder.appName('Storing and/or Loading Data').getOrCreate()


def store_data():
	df = read_file('data_batch_transformed')
	engine = create_engine(db_engine)
	df.toPandas().to_sql(batch_table, engine, schema=db_schema, if_exists='append', index=False)


def load_data():
	GET_ALL_SQL = f'SELECT * FROM {db_schema}.{batch_table};'
	df = pd.read_sql(GET_ALL_SQL, engine)
	return df
