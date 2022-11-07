import pickle

def load_model():
	global model
	model = pickle.load(open('../model/suicide_model.pkl', 'rb'))