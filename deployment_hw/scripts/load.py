import pickle

def load_model():
	model = pickle.load(open('./model/suicide_model.pkl', 'rb'))

	return model