
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
    if data.has_key('id'):
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