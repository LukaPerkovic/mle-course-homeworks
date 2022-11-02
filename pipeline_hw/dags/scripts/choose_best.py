import glob
import os

import shutil

MODEL_DIR = '/opt/airflow/models/'
BEST_MODEL_DIR = '/opt/airflow/best_model/'


def choose_best():
	model_path = ''
	score = 0

	for file in os.listdir(MODEL_DIR):
		if file.startswith('model'):
			model_score = int(file[-6:-4])

			if model_score > score:
				score = model_score
				model_path = file	

	origin_filepath = os.path.join(MODEL_DIR, model_path)
	destination_filepath = os.path.join(BEST_MODEL_DIR, model_path)		

	for f in os.listdir(BEST_MODEL_DIR):
		os.remove(os.path.join(BEST_MODEL_DIR, f))

	shutil.copyfile(origin_filepath, destination_filepath)

	return True
