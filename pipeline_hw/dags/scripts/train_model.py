import os
import numpy as np
import datetime
import logging


from scripts.handle_file import read_file
from scripts.handle_model import save_model
from scripts.modeling import modeling

MODEL_DIR = '/opt/airflow/models/'


def train_model():
	df = read_file('data_batch_transformed.csv')


	model, percentage = modeling(df)

	actual_date = datetime.datetime.now().strftime('%Y%m%d%H%M')
	trained = 't'
	filename = f'model_{trained}_{actual_date}_{percentage}.pkl'

	save_model(model, os.path.join(MODEL_DIR, filename))


	return True
