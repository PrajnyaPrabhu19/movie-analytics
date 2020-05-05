import os
from Modules import ParseDataset
###
    ## This file contains methods to support import/export functionality
###


###
    ## Helper function to convert a list to a string. Key fields in moviesData with a list value
    ## are passed in as a parameter and converted to a single '|' separated string.
    ## The fields include cast, keywords, genres, and production_companies
###
def createString(field_data):
    try:
        if type(field_data) == list:
            listToStr = '|'.join(field_data)
        else:
            listToStr = '|'.join(field_data.split(','))
    except Exception as e:
        print(e)
    return listToStr


##
    ## importData function returns a new moviesData list.
    ## This function takes a .csv filename as user input and loads that data into moviesData
##
def importData(filename):
    filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/Data/" + filename
    moviesData = ParseDataset.parseCSV(filepath)
    return moviesData


##
    ## exportData function converts moviesData back into a CSV file.
    ## This function takes a .csv filename from user input and converts the current moviesData
    ## to csv format and loads it into 'filename.csv'.
##
def exportData(filename, moviesData):
    row = ''
    filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/Data/" + filename
    fields = "id,imdb_id,popularity,budget,revenue,original_title,cast,homepage,director,tagline," \
                   "keywords,runtime,genres,production_companies,release_date,vote_count,vote_average," \
                   "release_year,budget_adj,revenue_adj\n"

    with open(filepath, 'w+', encoding='utf8', newline='') as f:
        f.write(fields)
        for movie in moviesData:
            for key in movie:
                # Keys that contain lists in their data fields.
                if key == 'cast': #or key == 'keywords'  or key == 'production_companies'  or key == 'genres'
                    row += createString(movie[key])
                    row += ','
                # Single value keys
                else:
                    row += str(movie[key])
                    row += ','
            # Delete comma at end of row
            row = row[:-1]
            f.write(row)
            row = ''
    f.close()
