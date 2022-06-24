import unittest
import pandas as pd
import sys
sys.path.append('../')

from forest.forest_model import ActualTreeModel


class TestActualTreeModel(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.filepath = '../forest/train.csv'
		cls.model = 'rf'
		cls.scaler = 'standard'

	def setUp(self):
		self.tree = ActualTreeModel()

	def test_data_load(self):
		self.tree.load_data(self.filepath)

		self.assertIsNotNone(self.tree.df)
		self.assertIsNotNone(self.tree.X_train)
		self.assertIsNotNone(self.tree.X_test)
		self.assertIsNotNone(self.tree.y_train)
		self.assertIsNotNone(self.tree.y_test)

	def test_pipeline(self):
		self.tree.load_data(self.filepath)
		self.tree.set_pipeline(self.scaler,self.model)
		self.assertEqual(self.tree.pipeline.steps[0][0],
					'column_transformer')
		self.assertEqual(self.tree.pipeline.steps[1][0],
					'model')

	def test_score(self):
		self.tree.load_data(self.filepath)
		self.tree.set_pipeline(self.scaler, self.model)
		score = self.tree.get_score()
		self.assertGreater(score, 0.80)


if __name__ == '__main__':
	if len(sys.argv) > 1:
		TestActualTreeModel.model = sys.argv.pop()
		TestActualTreeModel.scaler = sys.argv.pop()
	unittest.main()
