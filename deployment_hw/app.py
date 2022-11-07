from flask import Flask, request

from scripts.load import load_model
from scripts.transform import transform
from scripts.serve import serve

app = Flask(__name__)


@app.route('/predict', methods=['GET', 'POST'])
def form_example():
	if request.method == 'POST':

		# Single
		country = request.form.get('country')
		sex = request.form.get('sex')
		age = request.form.get('age')

		# Batch
		csv = request.files.get('data')

		if csv:
			batch = True
			df = transform(csv, batch)
		elif not any(item is None for item in [str(country), str(sex), int(age)]):
			batch = False
			df = transform([country, sex, age], batch)

		score = serve(df, batch)

		if batch:
			return_string = f'The probabilities of these people killing themselves are: {score}\n' 
		else:
			return_string = f'The probabilty of this person killing themself is: {score}\n' 

		return return_string

	else:
		return '''
			<form method="POST">
				<div><label>Country <input type="text" name="country"></label></div>
				<div><label>Gender <input type="text" name="sex"></label></div>
				<div><label>Age <input type="number" name="age"></label></div>
				<input type="submit" value="Submit">
			</form>'''

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)