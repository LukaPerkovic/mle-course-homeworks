# pylint: disable=W0311,C0103,C0115,C0116,R0902


import pickle
import pandas as pd


def load_model():

    with open('./models/model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    return loaded_model


def get_accuracy(model, X, y):
    y_pred = model.predict(X)
    score = [1 if y_pred[i] == y[i] else 0 for i in range(len(y))]
    return round(sum(score) / len(score), 2)


test = pd.read_csv('./data/test.csv')
model = load_model()


metrics = get_accuracy(model, test.drop('Cover_Type', axis=1), test.Cover_Type)

with open("./results/metrics.txt", "w", encoding="utf-8") as f:
    f.write(f"Model score: {metrics}")
