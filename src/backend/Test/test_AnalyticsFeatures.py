import unittest
import os
import Modules
from Modules import SearchFeatures
from Modules import ParseDataset
from Modules import AnalyticsFeatures


class TestAnalyticsFeatures(unittest.TestCase):
    def test_searchFlopMovies(self):
        year = '2015'
        response = Modules.AnalyticsFeatures.searchFlopMovies(year, movies)
        self.assertEqual(response[0]['original_title'], 'Wild Card', "The returned response should contain movie Wild Card")


filepath = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "/Data/test_dataset.csv"
movies = Modules.ParseDataset.parseCSV(filepath)

if __name__ == '__main__':
    unittest.main()