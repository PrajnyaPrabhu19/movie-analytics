###
    ## This file contains all methods which are used to implement search features for the application
###



###
    ## fetchMoviesByPopularity function returns all movies whose popularity is higher/lesser or eaqual than the search_query
###
def fetchMoviesByPopularity(search_field, search_query, search_inequality, moviesData):
    # Code for operations
    operations = {
        '0': '=',
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
    ## searchFlopMovies function returns list of all movies whose budget is more than revenue
###
def searchFlopMovies(year, moviesData):
    responseObject = []
    for movie in moviesData:
        if movie['release_year'] == year:
            if float(movie['budget']) > float(movie['revenue']):

                responseObject.append(movie['original_title'])
    return responseObject

###
    ## searchHighestGrossing function returns the highest grossing movie (revenue - budget) of the year
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
