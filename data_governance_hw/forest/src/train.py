# pylint: disable=W0311,C0103,C0115,C0116,R0902
import pickle
import yaml
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

params = yaml.safe_load(open("params.yaml"))["train"]
model_type_arg = params['model_type']


def train_model(dataframe, target, model_type):
    model = None
    if model_type == "rf":
        model = RandomForestClassifier(
            criterion="log_loss",
            max_depth=15,
            min_samples_split=3,
            min_samples_leaf=1,
        )
    elif model_type == 'knn':
        model = KNeighborsClassifier(
            weights="distance", algorithm="kd_tree", leaf_size=10, p=1
        )

    model.fit(dataframe.drop(target, axis=1), dataframe[target])

    return model


df = pd.read_csv('./data/train.csv', delimiter=',')

trained_model = train_model(df, 'Cover_Type', model_type_arg)

with open('./models/model.pkl', 'wb') as file:
    pickle.dump(trained_model, file)
