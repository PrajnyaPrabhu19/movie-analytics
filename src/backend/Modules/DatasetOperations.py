
def getMaxId(moviesData):
    idlist = [x['id'] for x in moviesData]
    return max(idlist)


###
    ## insertMovie() function will allow user to add a new row to the dataset.
    ## assume that the request can have maximum of 20 features.
    ## keys that are not unique will have '0' values if they are integer fields or 'none' value if they are string and if
    ## the item is expected to be of type list, then an empty list is appended
###
def insertMovie(data, moviesData):
    #construct the dictionary with initial values
    movie = {'id': '0', 'imdb_id':'', 'popularity':'', 'budget':'', 'revenue':'', 'original_title':'',
                  'cast':[],'homepage':'','director':'', 'tagline':'', 'keywords':[],
                  'runtime':'', 'genres':[], 'production_companies':[], 'release_date':'', 'vote_count':'',
                  'vote_average':'', 'release_year':'', 'budget_adj':'', 'revenue_adj':''}

    if 'id' in data:
        movie['id'] = data['id']
    else:
        #get the max id from the moviesdata and add 1 to it to have a unique id
        max_id = getMaxId(moviesData)
        newid = int(max_id)+1
        movie['id'] = str(newid)

    for key in data:
        if key!= 'id':
            movie[key] = data[key]
    print(movie)
    moviesData.append(movie)
    return moviesData

###
    ## updateMovie() function will allow user to update an existing row in the dataset.
    ## Finds correct movie using a specified ID or movie title.
###
def updateMovie(data, moviesData):
    # Search by movie id or title
    if 'id' in data:
        searchKey = 'id'
    else:
        searchKey = 'original_title'

    for movie in moviesData:
        # Find movie to be updated
        if movie[searchKey] == data[searchKey]:
            # Update movie with new values
            for key in data:
                movie[key] = data[key]

    return moviesData


###
    ## deleteMovie function will allow user to delete the movie by id. The user will select the movie from the list displayed on the
    ## UI and click on delete button. 
###
def deleteMovie(data, moviesData):
    movie_id = data['id']
    moviesData = list(filter(lambda i: i['id'] != movie_id, moviesData))
    return moviesData
