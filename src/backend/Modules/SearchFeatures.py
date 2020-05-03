###
    ## This file contains all methods which are used to implement search features for the application
###


###
    ## fetchMoviesByNumericSearch function returns all movies whose search_field is higher/lesser or eaqual than the search_query
    ## This is a generic function which will accept a search_field whose value is numeric and returns data whise values satisfy the
    ## search_inequality with the search_query
###
def fetchMoviesByNumericSearch(search_field, search_query, search_inequality, moviesData):
    # Code for operations
    operations = {
        '0': '==',
        '1': '>',
        '2': '>=',
        '3': '<',
        '4': '<='
    }
    responseObject = []

    for movie in moviesData:
        try:
            if (eval(movie[search_field] + operations[search_inequality] + search_query)):
                responseObject.append(movie)

        except Exception as e:
            print(e)
    return responseObject

###
    ## fetchMoviesByTextSearchfunction returns all movies whose search_field matches the search_query
    ## This is a generic function which handles text search_field
###
def fetchMoviesByTextSearch(search_field, search_query, moviesData):
    responseObject = []

    for movie in moviesData:
        # check if the search field is genre as it is a list
        if type(movie[search_field])==list:
            stringList=""
            for item in movie[search_field]:
                stringList+=item
            if search_query.lower() in stringList.lower():
                responseObject.append(movie)
        else:
            if  search_query.lower() in movie[search_field].lower():
                responseObject.append(movie)
    #if len(responseObject) ==0:
        #responseObject.append({"message":"No search results for given criteria"})
    return responseObject


###
    ## highestGrossingMovie function returns the highest grossing movie (revenue - budget) of the year
###
def highestGrossingMovie(year, moviesData):
    responseObject = ""
    _grossIncome = 0
    maxGross = 0
    # For now just returns title of movie, may change to return list with additional info
    for movie in moviesData:
        if movie['release_year'] == year:
            _grossIncome = float(movie['revenue']) - float(movie['budget'])
            if _grossIncome > maxGross:
                maxGross = _grossIncome
                responseObject = movie['original_title']
    return responseObject

###
    ## highestGrossingDirector function returns the highest grossing director (revenue - budget) of the year
###
def highestGrossingDirector(year, moviesData):
    responseObject = ""
    _movieProfit = 0
    highestProfit = 0
    for movie in moviesData:
        if movie['release_year'] == year:
            _movieProfit = float(movie['revenue']) - float(movie['budget'])
            if _movieProfit > highestProfit:
                highestProfit = _movieProfit
                responseObject = movie['director']
    return responseObject

def highestGrossingActorYear(year, moviesData):
    actorDict = {}
    responseObject = ""
    for movie in moviesData:
        if movie['release_year'] == year:
            rev = float(movie['revenue'])
            for i in movie['cast']:
                if i in actorDict.keys():
                    actorDict[i] += rev
                else:
                    actorDict[i] = rev
    responseObject = max(actorDict, key=lambda k: actorDict[k])
    return responseObject

