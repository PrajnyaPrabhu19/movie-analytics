###
    # Function to split the string from a column in dataset into multiple items and add it to a list
###

def createListofItems(row,split):
    words = row.split(split)
    listofItems = []
    for item in words:
        listofItems.append(item)

    return listofItems

###
    # Function to split each row from dataset and construct a dictionary
    # In this function we read character by character and check for delimiters.
    # There are few columns which are string literals. 'singleColumnData' is a boolean flag which will identify such strings and any delimiters
    # present inside this string will be ignored until a " is encountered.
###

def buildMovieDict(line):
    row =[]
    word =''
    singleColumnData = False
    for i in range(len(line)):

        if singleColumnData:
            if line[i] != "\"":
                word += line[i]
            else:
                row.append(word)
                word=''
                singleColumnData = False
        else:
            #check for delimiter
            if ((line[i] != ",") ):
                #check for first " - this indicates start of string data in the row of dataset
                if line[i]=="\"":
                    singleColumnData = True
                else:
                    word += line[i]
            else:
                if line[i-1] != "\"":
                    row.append(word)
                    word=''
    #append the last collected word to list
    row.append(word)

    actors = createListofItems(row[6], '|')

    keywords = createListofItems(row[10], '|')

    genres = createListofItems(row[12], '|')

    production_companies = createListofItems(row[13],'|')

    # few of the data types mentioned which will be present in the dictionary
    # homepage is the link, cast is list of actors, keywords is list of keywords for the movie, runtime in minutes, genre is a list
    # production_companies is a list of production companies for a given movie

    movieDict = { 'id': row[0], 'imdb_id':row[1], 'popularity':row[2], 'budget':row[3], 'revenue':row[4], 'original_title':row[5],
                  'cast':actors,'homepage':row[7],'director':row[8], 'tagline':row[9], 'keywords':keywords,
                  'runtime':row[11], 'genres':genres, 'production_companies':production_companies, 'release_date':row[14], 'vote_count':row[15],
                  'vote_average':row[16], 'release_year':row[17], 'budget_adj':row[18], 'revenue_adj':row[19]}

    return movieDict

###
    # Function to imitate the read_csv() method;
    # Here each line from the file is read and a dictioanry is created. Final returnable object is a list of dictionaries.
###

def parseCSV(filePath):
    #TODO: check if the filepath is valid and the file exists

    with open(filePath) as f:
        movies = []
        next(f)
        for line in f:
            data = buildMovieDict(line)
            movies.append(data)

    f.close()
    return movies