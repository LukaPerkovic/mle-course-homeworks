import os
import numpy as np
from datetime import datetime
import logging

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from scripts.handle_data import load_data
from scripts.handle_model import save_model


DATA_DIR = '/opt/airflow/data/'


def retrain_model():
	df = load_data()

	logging.warn(f'Database dimensions: {df.shape}')

	cv = KFold(n_splits=10, random_state=1, shuffle=True)


	model = RandomForestClassifier(
		criterion='log_loss',
		max_depth=15,
		min_samples_split=3,
		min_samples_leaf=1
		)


	scores = cross_val_score(model, df.drop('Cover_Type', axis=1), df.Cover_Type, scoring='accuracy', cv=cv, n_jobs=1, error_score='raise')

	logging.warn(f'Prediction scores: {scores}')

	percentage = str(int(round(np.mean(scores), 2) * 100))

	actual_date = datetime.date.today().strftime('%Y%m%d')
	rtrained = 'rt'
	filename = f'{model}_{trained}_{actual_date}_{percentage}'

	save_model(filename)


	return True
