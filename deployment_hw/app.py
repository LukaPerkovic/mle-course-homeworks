from flask import Flask, request

from scripts.transform import transform

app = Flask(__name__)


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
	if request.method == 'POST':
		country = request.form.get('country')
		sex = request.form.get('sex')
		age = request.form.get('age')
		csv = request.files.get('data')
		if csv:
			batch = True
			df = transform(csv, batch)
		elif not any(item is None for item in [country, sex, age]):
			df = transform(csv, batch)

		score = serve(df, batch)
		if batch:
			return_string = 'The probabilities of these people killing themselves are: {score}' 
		else:
			return_string = 'The probabilty of this person killing themself is: {score}' 

		return return_string
		
		else:
			return f"Error in POST control flow: [{country}, {sex}, {age}, {csv}]"
	else:
		return '''
			<form method="POST">
				<div><label>Country <input type="text" name="country"></label></div>
				<div><label>Gender <input type="text" name="sex"></label></div>
				<div><label>Age <input type="number" name="age"></label></div>
				<input type="submit" value="Submit">
			</form>'''
		
@app.route('/json-example')
def json_example():
	return 'JSON Object Example'

if __name__ == '__main__':
	app.run(debug=True, port =5000)