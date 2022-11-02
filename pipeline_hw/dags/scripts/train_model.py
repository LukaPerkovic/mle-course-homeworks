import os
import numpy as np
from datetime import datetime
import logging


from scripts.handle_file import read_file
from scripts.handle_model import save_model
from scripts.modeling import modeling

def train_model():
	df = read_file('data_batch_transformed.csv')


	model, percentage = modeling(df)

	actual_date = datetime.date.today().strftime('%Y%m%d')
	trained = 't'
	filename = f'model_{trained}_{actual_date}_{percentage}'

	save_model(filename)


	return True
