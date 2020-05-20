import unittest
import os
import Modules
from Modules import ParseDataset

class TestParseCSV(unittest.TestCase):
    def test_parseCSV(self):
        filepath = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "/Data/test_dataset.csv"
        responseObject = Modules.ParseDataset.parseCSV(filepath)
        size = len(responseObject)
        # assert the size of response object with 3 as we know that the test dataset has only 2 rows.
        self.assertEqual(size, 3, "The data response object should have 2 items")
        invalid_filepath= os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "/Data/test_dataset_invalid.csv"
        responseObject = Modules.ParseDataset.parseCSV(invalid_filepath)
        size = len(responseObject)
        self.assertEqual(size , 1, "The response object should have one item with error message")
        item = responseObject[0]
        print(item)
        self.assertEqual(item , "Invalid filepath passed or no such file exists", "Check parseCSV() for invaild filepath")

    def test_buildMovieDict(self):
        line = '15239,tt0090190,0.335414,0,0,The Toxic Avenger,Mitch Cohen|Andree Maranda|Jennifer Prichard|Cindy Manion|Robert Prichard,,Lloyd Kaufman|Michael Herz,He was 98lbs. of solid nerd until he became...,corruption|mayor|anti hero|sadism|toxic waste,82,Science Fiction|Action|Comedy|Horror,Troma Entertainment,5/1/1984,51,6.2,1984,0.0,0.0'
        movieDict = Modules.ParseDataset.buildMovieDict(line)
        self.assertEqual(len(movieDict),20,"The movie dictionary object should have 20 items")
        self.assertEqual(int(movieDict['id']),15239, "The id should be 15239 from the line test sample.")

    def test_createListofItems(self):
        row='Mitch Cohen|Andree Maranda|Jennifer Prichard'
        split='|'
        listOfItems = Modules.ParseDataset.createListofItems(row, split)
        self.assertEqual(len(listOfItems),3,"There should be 3 items in the list from the test sample")


if __name__ == '__main__':
    unittest.main()