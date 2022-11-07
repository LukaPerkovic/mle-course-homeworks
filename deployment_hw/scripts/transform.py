import pandas as pd

from params import PARAMS, age_ranger

def transform(data_obj, batch=False) -> pd.DataFrame:

	# Initialization
	df = pd.DataFrame(data_obj)

	if not batch:
		df = df.T
		df.columns = ['country', 'sex', 'age']


	# Transformation
	df['country'] = df.country.apply(lambda x:x.lower())
	df['country'] = df.country.replace(PARAMS['country_list'])	
	df['sex'] = df.sex.replace(PARAMS['sex_list'])
	df['age'] = df.age.replace(age_ranger)

	return df
