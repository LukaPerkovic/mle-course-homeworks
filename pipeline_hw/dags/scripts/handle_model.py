import os
import pickle

MODEL_DIR = '/models/'

def save_model(model_name):
	pickle.dump(model, open(os.path.join(MODEL_DIR, model_name), 'wb'))

def load_model(model_name):
	pass
