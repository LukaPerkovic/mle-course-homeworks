from flask import Flask, request

app = Flask(__name__)

@app.route('/query-example')
def query_example():
	country = request.args.get('country')
	sex = request.args.get('sex')
	age = request.args.get('age')

	return f'Query String query_example: Array [{country} {sex} {age}]'

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
	if request.method == 'POST':
		country = request.form.get('country')
		sex = request.form.get('sex')
		age = request.form.get('age')
		csv = request.files.get('data')
		if csv:
			return 'Got the csv'
		elif not any(item is None for item in [country, sex, age]):
			return f'form Data Example: Array [{country} {sex} {age}]'
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