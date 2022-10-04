import sys
import warnings

import pandas as pd
import numpy as np

from load import BikeRentalDataLoader
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import IsolationForest, RandomForestRegressor, GradientBoostingRegressor

import mlflow
import mlflow.sklearn
from urllib.parse import urlparse

import logging

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


class BikeRegressor:
    def __init__(self):
        self.model_fitted = False
        self.model = None
        self.score = None

    @staticmethod
    def preprocess(dataframe: pd.DataFrame) -> dict:
        dataframe.drop(["dteday", "casual", "registered"], axis=1, inplace=True)
        X = dataframe.drop("cnt", axis=1)
        y = dataframe["cnt"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
        scaler = MinMaxScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.fit_transform(X_test)

        return {
            "X_train": X_train,
            "X_test": X_test,
            "y_train": y_train,
            "y_test": y_test,
        }

    @staticmethod
    def remove_outliers(data_dict: dict) -> dict:
        iso = IsolationForest(contamination=0.2)
        isofilter_train = iso.fit_predict(data_dict.get("X_train"))
        isofilter_test = iso.fit_predict(data_dict.get("X_test"))

        data_dict["X_train"] = data_dict["X_train"][isofilter_train != -1]
        data_dict["y_train"] = data_dict["y_train"][isofilter_train != -1]
        data_dict["X_test"] = data_dict["X_test"][isofilter_test != -1]
        data_dict["y_test"] = data_dict["y_test"][isofilter_test != -1]

        return data_dict

    def train_model(
        self,
        X_train: pd.DataFrame,
        y_train: pd.DataFrame,
        model: str,
        hyperparameter: dict
    ) -> True:

        if model == 'randomforest':

            model = RandomForestRegressor(
                n_estimators=int(list(hyperparameter.values())[0]))
        else:
            model = GradientBoostingRegressor(learning_rate=list(hyperparameter.values())[0])

        self.model = model.fit(X_train, y_train)

        return True

    def score_model(self, X_test: pd.DataFrame, y_test: pd.DataFrame) -> float:

        y_pred = self.model.predict(X_test)
        self.score = mean_absolute_error(y_test, y_pred)

        return self.score


def run_randomforest_regression(**arguments):



    bike_rental_data = BikeRentalDataLoader()
    bike_regressor = BikeRegressor()

    data = bike_regressor.preprocess(dataframe=bike_rental_data.get_data())
    if arguments.get('outliers') == 'exclude':
        data = bike_regressor.remove_outliers(data)

    bike_regressor.model_fitted = bike_regressor.train_model(
        data.get("X_train"),
        data.get("y_train"),
        arguments.get('model'),
        arguments.get('hyperparameter')
    )

    if bike_regressor.model_fitted:
        score = bike_regressor.score_model(data.get("X_test"), data.get("y_test"))
    else:
        
        logger.error("Model training process unsuccessful!")
        raise Exception

    return score, bike_regressor.model


if __name__ == "__main__":

    warnings.filterwarnings("ignore")

    try:
        model_name = str(sys.argv[1]).lower()
        hyperparameter = float(sys.argv[2])
        outliers = str(sys.argv[3]).lower()
    except Exception:
        raise Exception('Wrong arguments in input')


    if model_name == 'randomforest':
        hyperparam_dict = {"n_estimators": hyperparameter}
    else:
        hyperparam_dict = {"learning_rate": hyperparameter}
    
    mlflow.set_tracking_uri('http://127.0.0.1:5000')
    with mlflow.start_run():

        mae, model = run_randomforest_regression(
                                            model=model_name,
                                            hyperparameter=hyperparam_dict,
                                            outliers=outliers
        )

        print(f'MAE score is: {mae}')

    #     # MLFLOW part


        mlflow.log_param("Model", model)
        mlflow.log_param(f"{list(hyperparam_dict.keys())[0]}", list(hyperparam_dict.values())[0])
        mlflow.log_param("Remove outliers", outliers)
        mlflow.log_metric("MAE", mae)

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        if tracking_url_type_store != "file":
            mlflow.sklearn.log_model(
                model, "model", registered_model_name=f"{model_name}"
            )
        else:
            mlflow.sklearn.log_model(model, f"{model_name}")