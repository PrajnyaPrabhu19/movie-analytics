import os
from Modules import ParseDataset
##
    ## This file contains methods to support import/export functionality
##

def importData(filename):
    filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/Test/Data/" + filename + ".csv"
    moviesData = ParseDataset.parseCSV(filepath)
    return moviesData

def exportData():

    return
