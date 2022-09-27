import sys
import warnings

import pandas as pd
import numpy as np

from sklearn_regressor.load import BikeRentalDataLoader
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import IsolationForest, RandomForestRegressor

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
        dataframe.drop(["casual", "registered"], axis=1, inplace=True)
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
        n_estimators: int,
        max_depth: int,
        min_samples_split: int,
    ) -> True:

        model = RandomForestRegressor(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
        )

        self.model = model.fit(X_train, y_train)

        return True

    def score(self, X_test: pd.DataFrame, y_test: pd.DataFrame) -> float:

        y_pred = self.model(X_test)
        self.score = mean_absolute_error(y_test, y_pred)

        return self.score


def run_randomforest_regression(**arguments):

    bike_rental_data = BikeRentalDataLoader()
    bike_regressor = BikeRegressor()

    data = bike_regressor.preprocess(dataframe=bike_rental_data.get_data())
    data = bike_regressor.remove_outliers(data)

    bike_regressor.train_model(
        data.get("X_train"),
        data.get("y_train"),
        arguments.get("n_estimators"),
        arguments.get("max_depth"),
        arguments.get("min_samples_split"),
    )

    if bike_regressor.model_fitted:
        score = bike_regressor.score(data.get("X_test"), data.get("y_test"))
    else:
        logger("Model training process unsuccessful!")

    return score, bike_regressor.model


if __name__ == "__main__":

    warnings.filterwarnings("ignore")

    n_estimators = float(sys.argv[1]) if len(sys.argv) > 1 else 100
    max_depth = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
    min_samples_split = float(sys.argv[3]) if len(sys.argv) > 3 else 2

    with mlflow.start_run():

        mae, model = run_randomforest_regression(
            n_estimators, max_depth, min_samples_split
        )

        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("min_samples_split", min_samples_split)
        mlflow.log_metric("mae", mae)

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # TODO Figure out how model registry works
        if tracking_url_type_store != "file":

            # Register the model
            # There are other ways to use the Model Registry, which depends on the use case,
            # please refer to the doc for more information:
            # https://mlflow.org/docs/latest/model-registry.html#api-workflow
            mlflow.sklearn.log_model(
                model, "model", registered_model_name="RandomForestRegressor"
            )
        else:
            mlflow.sklearn.log_model(model, "model")
