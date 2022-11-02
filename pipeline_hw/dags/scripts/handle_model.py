import os
import pickle
from scripts.handle_file import delete_file


def save_model(model, path):
	if os.path.exists(path):
		pass
	else:
		pickle.dump(model, open(path, 'wb'))

def load_model(path):
	loaded_model = pickle.load(open(path))
	return loaded_model
