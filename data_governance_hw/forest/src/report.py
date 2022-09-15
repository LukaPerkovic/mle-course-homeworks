import matplotlib.pyplot as plt
import pandas as pd
from sklearn.inspection import permutation_importance
from evaluate import load_model


def generate_feature_importance_graph(model, test_data, test_target):

    perm_importance = permutation_importance(model, test_data, test_target)
    sorted_idx = perm_importance.importances_mean.argsort()

    plt.barh(
        [f"Feature {i}" for i in sorted_idx],
        perm_importance.importances_mean[sorted_idx],
    )
    plt.xlabel("Permutation Importance")
    plt.tight_layout()
    plt.savefig("./results/feature_importance.png", dpi=120)

if __name__ == "__main__":
    test = pd.read_csv('./data/test.csv')
    model = load_model()

    generate_feature_importance_graph(model, test.drop('Cover_Type', axis=1), test.Cover_Type)
