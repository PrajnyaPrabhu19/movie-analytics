import unittest
import os
import Modules

class TestSearchFeatures(unittest.TestCase):
    def test_fetchMoviesByNumericSearch(self):
        search_field = 'popularity'
        search_query = '31'
        search_inequality ='2'
        response = Modules.SearchFeatures.fetchMoviesByNumericSearch(search_field,search_query,search_inequality,movies)
        self.assertEqual(len(response), 1, "There should be one item satisfying the searched criteria")
        self.assertEqual(response['original_title'], 'Jurassic World', "The movie name returned by the response should be Jurassic World")


    def test_fetchMoviesByTextSearch(self):
        search_field='director'
        search_query='George Miller'
        response = Modules.SearchFeatures.fetchMoviesByTextSearch(search_field, search_query, movies)
        self.assertEqual(response['original_title'], 'Mad Max: Fury Road', "The returned response should contain movie Mad Max: Fury Road")


    def test_searchFlopMovies(self):
        year = '2015'
        response = Modules.SearchFeatures.searchFlopMovies(year, movies)
        self.assertEqual(response['original_title'], 'Wild Card', "The returned response should contain movie Wild Card")


filepath = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "/Data/test_dataset.csv"
movies = Modules.ParseDataset.parseCSV(filepath)

if __name__ == '__main__':
    unittest.main()