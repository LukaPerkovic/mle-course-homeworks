def serve(df, batch):

	score = [str(round(x*100, 2)) + '%' for x in model.predict(df)]

	return score[0] if batch else score

