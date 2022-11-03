import os
import numpy as np
import datetime


from scripts.handle_data import load_data
from scripts.handle_model import save_model
from scripts.modeling import modeling


MODEL_DIR = '/opt/airflow/models/'

def retrain_model():
	df = load_data()

	model, percentage = modeling(df)

	actual_date = datetime.datetime.now().strftime('%Y%m%d%H%M')
	trained = 'rt'
	filename = f'model_{trained}_{actual_date}_{percentage}.pkl'

	save_model(model, os.path.join(MODEL_DIR, filename))


	return True