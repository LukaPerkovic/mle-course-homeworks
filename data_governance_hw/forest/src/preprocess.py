# pylint: disable=W0311,C0103,C0115,C0116,R0902

import argparse
import os
import yaml
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer


parser = argparse.ArgumentParser(description="Get path to the dataset")
parser.add_argument("filename", type=str, help="Name to the dataset file")
args = parser.parse_args()
filename = args.filename

params = yaml.safe_load(open("params.yaml"))["preprocess"]
scaler_type = params['scaler']


def load_data(path_to_data, filetype="csv"):
    if filetype == "csv":
        dataframe = pd.read_csv(path_to_data)

    return dataframe


def transform_data(df):

    if scaler_type == "standard":
        scaler = StandardScaler()
    elif scaler_type == 'minmax':
        scaler = MinMaxScaler()

    soil_cols = [name for name in df.columns if name.startswith("Soil")]
    wilderness_cols = [name for name in df.columns if name.startswith("Wild")]
    hillshade_cols = [name for name in df.columns if name.startswith("Hill")]
    restof_columns = [
        "Elevation",
        "Aspect",
        "Slope",
        "Horizontal_Distance_To_Hydrology",
        "Vertical_Distance_To_Hydrology",
        "Horizontal_Distance_To_Roadways",
    ]

    col_transform = ColumnTransformer(
        [
            ("rest", scaler, restof_columns),
            ("soil", PCA(n_components=7), soil_cols),
            ("wild", PCA(n_components=3), wilderness_cols),
            ("hill", PCA(n_components=1), hillshade_cols),
        ]
    )

    return col_transform.fit_transform(df)


df = load_data(os.path.join('./data/', filename))
train_raw, test_raw = train_test_split(df, test_size=0.33)
train_raw.reset_index(drop=True, inplace=True)
test_raw.reset_index(drop=True, inplace=True)
train, test = transform_data(train_raw.drop(
    'Cover_Type', axis=1)), transform_data(test_raw.drop('Cover_Type', axis=1))

train = pd.DataFrame(data=train, columns=[
                     f'feature {i}' for i in range(1, train.shape[1]+1)])
test = pd.DataFrame(data=test, columns=[
                    f'feature {i}' for i in range(1, test.shape[1]+1)])

train['Cover_Type'] = train_raw.Cover_Type
test['Cover_Type'] = test_raw.Cover_Type

train.to_csv('./data/train.csv')
test.to_csv('./data/test.csv')
