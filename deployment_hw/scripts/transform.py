import pandas as pd

from scripts.params import PARAMS, age_ranger

def transform(data_obj, batch=False) -> pd.DataFrame:

	# Initialization
	if batch:
		df = pd.read_csv(data_obj)

	else:
		df = pd.DataFrame(data_obj).T
		df.columns = ['country', 'sex', 'age']

	 # Transformation
		
	df['country'] = df.country.apply(lambda x:x.lower())
	df['country'] = df.country.replace(PARAMS['country_list'])
	df['sex'] = df.sex.replace(PARAMS['sex_list'])
	df['age'] = pd.to_numeric(df['age'])
	df['age'] = df.age.apply(age_ranger)



	return df
