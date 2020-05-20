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
        self.assertEqual(response['data'][0]['original_title'], 'Wild Card', "The returned response should contain movie Wild Card")

    def test_highestGrossingMovie(self):
        year = '2015'
        response = Modules.AnalyticsFeatures.highestGrossingMovie(year, movies)
        self.assertEqual(response['data'][0]['original_title'], 'Jurassic World', "The response should contain Jurassic World movie")

    def test_moviesAggregate(self):
        response = Modules.AnalyticsFeatures.moviesAggregate(movies)
        self.assertEqual(response['data'][7]['year'], '2009-2015', "The response should have year 2009-2015")
        self.assertEqual(response['data'][7]['budget'], 330000000.0, "The response ahould have the budget value 330000000.0")

    def test_analyticsGenre(self):
        year = '2015'
        response = Modules.AnalyticsFeatures.analyticsGrenre(year, movies)
        self.assertEqual(response['data']['RECORDS'][0]['total_amt'], 1591965164.0, "The response should have total amount as 1591965164.0")

    def test_actorGenres(self):
        actorName = 'Chris Pratt'
        response = Modules.AnalyticsFeatures.actorGenres(actorName, movies)
        self.assertEqual(response['data']['values'][0], 1, "The response should have value 1")

    def test_directorGenres(self):
        dirName = 'Colin Trevorrow'
        response = Modules.AnalyticsFeatures.directorGenres(dirName, movies)
        self.assertEqual(response['data']['values'][0], 1, "The response should have value 1")

    def test_actorTrajectory(self):
        actor = 'Chris Pratt'
        response = Modules.AnalyticsFeatures.actorTrajectory(actor, movies)
        self.assertEqual(response['data'][0]['revenue'], 1513528810.0, "The response should have revenue 1513528810.0")

    def test_directorTrajectory(self):
        director = 'Colin Trevorrow'
        response = Modules.AnalyticsFeatures.directorTrajectory(director, movies)
        self.assertEqual(response['data'][0]['revenue'], 1513528810.0, "The response should have revenue 1513528810.0")

filepath = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "/Data/test_dataset.csv"
movies = Modules.ParseDataset.parseCSV(filepath)

if __name__ == '__main__':
    unittest.main()