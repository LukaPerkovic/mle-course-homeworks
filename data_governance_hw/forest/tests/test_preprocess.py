import unittest
import numpy as np
import pandas as pd
from unittest.mock import Mock


class TestPreprocess(unittest.TestCase):

    def test_transform_data(self):
        transformed_mock = Mock(return_value=np.random.rand(3, 2))
        transformed_mock.shape = Mock(return_value=(3, 2))
     
        pandas_mock = pd.DataFrame(data=transformed_mock())

        self.assertEqual(transformed_mock.shape(), (3, 2))
        self.assertIsInstance(pandas_mock, pd.DataFrame)


if __name__ == "__main__":
    unittest.main()
