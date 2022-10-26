import glob
import os

import shutil


MODEL_DIR = '/models/'
BEST_MODEL_DIR = '/best_model/'


def choose_best():
	model = ''
	score = 0

	for file in os.listdir('.'):
		model_score = int(file[-2:])

		if model_score > score:
			score = model_score
			model = file	

	origin_filepath = os.path.join(MODEL_DIR, model)
	destination_filepath = os.path.join(BEST_MODEL_DIR, model)		

	for f in os.listdir(BEST_MODEL_DIR):
		os.remove(os.path.join(BEST_MODEL_DIR, f))

	shutil.copyfile(origin_filepath, destination_filepath)

	return True
