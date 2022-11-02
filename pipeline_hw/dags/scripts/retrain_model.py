import os
import numpy as np
import datetime


from scripts.handle_data import load_data
from scripts.handle_model import save_model
from scripts.modeling import modeling

def retrain_model():
	df = load_data()

	model, percentage = modeling(df)

	actual_date = datetime.date.today().strftime('%Y%m%d')
	trained = 'rt'
	filename = f'model_{trained}_{actual_date}_{percentage}'

	save_model(model, filename)


	return True