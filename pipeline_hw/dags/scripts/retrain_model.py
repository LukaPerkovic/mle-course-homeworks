import os
import numpy as np
from datetime import datetime


from scripts.handle_data import load_data
from scripts.handle_model import save_model
from scripts.modeling import modeling

def retrain_model():
	df = load_data()

	model, percentage = modeling(df)

	actual_date = datetime.date.today().strftime('%Y%m%d')
	rtrained = 'rt'
	filename = f'model_{trained}_{actual_date}_{percentage}'

	save_model(filename)


	return True
