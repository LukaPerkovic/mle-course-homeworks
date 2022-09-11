"""
Model for classfying the type of tree and providing the feature importance graph and a text file.
It accpets arguments for type of model, and type of standardization.
"""

import argparse
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.inspection import permutation_importance


parser = argparse.ArgumentParser(description="Experiments with model")
parser.add_argument("model", type=str, help="rf or knn")
parser.add_argument("scale", type=str, help="standard or minmax")
args = parser.parse_args()

model = args.model
scaler = args.scale


# pylint: disable=W0311,C0103,C0115,C0116,R0902

class ActualTreeModel:
    def __init__(self):
        self.df = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

        self.model = None
        self.scaler = None

        self.col_transform = None
        self.pipeline = None
        self.score = None

    def load_data(self, path_to_data, filetype="csv"):

        if filetype == "csv":
            self.df = pd.read_csv(path_to_data)

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.df.drop("Cover_Type", axis=1), self.df.Cover_Type
        )

    def set_pipeline(self, scaler_type, model_type):

        if scaler_type == "standard":
            self.scaler = StandardScaler()
        else:
            self.scaler = MinMaxScaler()

        if model_type == "rf":
            self.model = RandomForestClassifier(
                criterion="log_loss",
                max_depth=15,
                min_samples_split=3,
                min_samples_leaf=1,
            )
        else:
            self.model = KNeighborsClassifier(
                weights="distance", algorithm="kd_tree", leaf_size=10, p=1
            )

        soil_cols = [name for name in self.df.columns if name.startswith("Soil")]
        wilderness_cols = [name for name in self.df.columns if name.startswith("Wild")]
        hillshade_cols = [name for name in self.df.columns if name.startswith("Hill")]
        restof_columns = [
            "Elevation",
            "Aspect",
            "Slope",
            "Horizontal_Distance_To_Hydrology",
            "Vertical_Distance_To_Hydrology",
            "Horizontal_Distance_To_Roadways",
        ]

        self.col_transform = ColumnTransformer(
            [
                ("rest", self.scaler, restof_columns),
                ("soil", PCA(n_components=7), soil_cols),
                ("wild", PCA(n_components=3), wilderness_cols),
                ("hill", PCA(n_components=1), hillshade_cols),
            ]
        )

        self.pipeline = Pipeline(
            [("column_transformer", self.col_transform), ("model", self.model)]
        )

    def get_score(self):

        self.pipeline.fit(self.X_train, self.y_train)
        self.score = self.pipeline.score(self.X_test, self.y_test)
        return self.score

    def generate_feature_importance_graph(self):

        mdl = self.pipeline.steps[-1][1]
        X_test_pipe = self.col_transform.transform(self.X_test)

        perm_importance = permutation_importance(mdl, X_test_pipe, self.y_test)
        sorted_idx = perm_importance.importances_mean.argsort()

        plt.barh(
            [f"Feature {i}" for i in sorted_idx],
            perm_importance.importances_mean[sorted_idx],
        )
        plt.xlabel("Permutation Importance")
        plt.tight_layout()
        plt.savefig("feature_importance.png", dpi=120)


if __name__ == "__main__":
    filepath = "train.csv"

    tree = ActualTreeModel()
    tree.load_data(filepath)
    tree.set_pipeline(scaler, model)
    score = tree.get_score()
    with open("metrics.txt", "w", encoding="utf-8") as f:
        f.write(f"Model score: {round(score,2)}")
    tree.generate_feature_importance_graph()
