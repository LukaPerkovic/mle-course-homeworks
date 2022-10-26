import glob

from scripts.validate_data import validate_target_variable
from scripts.handle_data import load_data
from scripts.handle_model import load_model

BEST_MODEL_DIR = '/best_model/'


def serve_model():

	pick_up_pickle = glob.glob('*.pkl')[0]
	model = load_model(pick_up_pickle)

	df = load_data()

	y = df.Cover_Type
	y_pred = mode.predict(df.drop('Cover_Type', axis=1))

	score = [1 if y_pred[i] == y[i] else 0 for i in range(len(y))]

	result = round(sum(score) / len(score), 2)

	print(results)

