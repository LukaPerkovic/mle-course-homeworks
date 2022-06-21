import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import argparse
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.inspection import permutation_importance
from sklearn.svm import LinearSVC
import shap


parser = argparse.ArgumentParser(description='Experiments with model')
parser.add_argument('model', type=str, help='rf or svc')
parse.add_argument('scale', type=str, help='standard or minmax')
args = parser.parse_args()

model = args.model
scaler = args.scale



class ActualTreeModel:

	def __init__(self):
		pass

	def load_data(self, path_to_data):
		pass

	def set_pipeline(self, scaler_type, model_type):
		pass

	def score(self, xtrain, xtest, ytrain, ytest):
		pass

	def generate_feature_importance_graph(self,model, pull_existing_test_data='yes'):
		pass





if __name__ == 'main':
	pass
