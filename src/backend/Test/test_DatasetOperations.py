import unittest
import os
import Modules
from Modules import DatasetOperations
from Modules import ParseDataset


class TestDatasetOperations(unittest.TestCase):
    def test_deleteMovie(self):
        data = {"id":"265208"}
        global movies
        initial_size = len(movies)
        movies = DatasetOperations.deleteMovie(data, movies)
        self.assertEqual(len(movies), initial_size-1, "The delete operation failed")

    def test_insertData(self):
        data = {"id":"423", "popularity":"2", "budget":"3000","revenue": "5000", "original_title":"Test new movie"}
        global movies
        initial_size = len(movies)
        movies = DatasetOperations.insertMovie(data, movies)
        self.assertEqual(len(movies)-1, initial_size, "Insert failed")

filepath = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "/Data/test_dataset.csv"
movies = Modules.ParseDataset.parseCSV(filepath)

if __name__ == '__main__':
    unittest.main()