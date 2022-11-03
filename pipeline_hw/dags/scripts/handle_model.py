import os
import pickle


def save_model(model, path):
	if os.path.exists(path):
		pass
	else:
		pickle.dump(model, open(path, 'wb'))

def load_model(path):
	loaded_model = pickle.load(open(path, 'rb'))
	return loaded_model
