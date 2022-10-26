import os
import pickle

MODEL_DIR = '/models/'

def save_model(model_name):
	pickle.dump(model, open(os.path.join(MODEL_DIR, model_name), 'wb'))

def load_model(model_name):
	pass
import os
import pickle

BEST_MODEL_DIR = '/best_model/'

def save_model(model_name):
	pickle.dump(model, open(os.path.join(BEST_MODEL_DIR, model_name), 'wb'))

def load_model(model_name):
	loaded_model = pickle.load(open(os.path.join(BEST_MODEL_DIR, model_name)))
	return loaded_model