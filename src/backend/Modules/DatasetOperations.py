
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
    #construct the dictionary
    movie = {}
    if 'id' in data:
        movie['id'] = data['id']
    else:
        #get the max id from the moviesdata and add 1 to it to have a unique id
        max_id = getMaxId(moviesData)
        movie['id'] = max_id+1

    for key in data:
        if key!= 'id':
            movie[key] = data[key]
    moviesData.append(movie)

    return moviesData


###
    ## updateMovie() function will allow user to update an existing row in the dataset.
    ## Finds correct movie using a specified ID or movie title.
    ##
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
