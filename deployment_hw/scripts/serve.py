from scripts.load import load_model

def serve(df, batch):
	try:		
		model = load_model()
		score = [str(round(x*100, 2)) + '%' for x in model.predict(df)]

	except ValueError:
		raise ValueError('Incorrect values supplied to the model!')

	return score if batch else score[0]

