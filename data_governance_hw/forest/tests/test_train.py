import unittest
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from unittest.mock import Mock
from src.train import train_model

class TestTrain(unittest.TestCase):

    def test_train_model(self):

        df = pd.DataFrame(np.random.randint(0,100, size=(100,4)), columns=list('ABCD'))

        # Test Random Forest
        rf = train_model(df, 'D', 'rf')

        # Test KNN 
        knn = train_model(df, 'D',  'knn')

        self.assertIsInstance(rf, RandomForestClassifier)
        self.assertIsInstance(knn, KNeighborsClassifier)


if __name__ == "__main__":
    unittest.main()
