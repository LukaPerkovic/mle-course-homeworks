import unittest
import numpy as np
import pandas as pd
from src.train import train_model
from src.evaluate import get_accuracy




class TestEvaluate(unittest.TestCase):

    def setUp(self):
        
        # First randomized dataframe
        df = pd.DataFrame(np.random.randint(0,100, size=(100,4)), columns=list('ABCD'))
        self.rf = train_model(df, 'D', 'rf')

        # Newly randomized dataframe
        self.test_df = pd.DataFrame(np.random.randint(0,100, size=(100,4)), columns=list('ABCD'))
    
    def test_evaluate(self):
        score = get_accuracy(self.rf, self.test_df.drop('D', axis=1), self.test_df.D)

        self.assertGreaterEqual(score, 0)
        self.assertLess(score, 0.999)

if __name__ == "__main__":
    unittest.main()
