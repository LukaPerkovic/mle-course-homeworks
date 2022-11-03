import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier



def modeling(df):

	cv = KFold(n_splits=5, random_state=1, shuffle=True)


	model = RandomForestClassifier(
		max_depth=15,
		min_samples_split=3,
		min_samples_leaf=1
		)


	scores = cross_val_score(model, df.drop('Cover_Type', axis=1), df.Cover_Type, scoring='accuracy', cv=cv, n_jobs=1)
	percentage = str(int(round(np.mean(scores), 2) * 100))

	model.fit(df.drop('Cover_Type', axis=1), df.Cover_Type)


	return model, percentage
