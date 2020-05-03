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
    ## searchFlopMovies function returns list of all movies whose budget is more than revenue
###
def searchFlopMovies(year, moviesData):
    responseObject = []
    for movie in moviesData:
        if movie['release_year'] == year:
            if float(movie['budget']) > float(movie['revenue']):
                if float(movie['revenue']) != 0:
                    diff = float(movie['budget'])- float(movie['revenue'])
                    movie['loss'] = diff
                    responseObject.append(movie)

    responseObject = sorted(responseObject, key = lambda i:i['loss'],reverse=True)
    responseObject = responseObject[:10]
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

def moviesAggregate(moviesData):
    response =[]
    #myMax = max(movie['release_year'] for movie in moviesData)
    #print(myMax)
    #myMin = min(movie['release_year'] for movie in moviesData)
    #print(myMin)
    myMin =1960
    myMax = 2015
    diff = float(myMax)-float(myMin)
    window = round(diff/5)
    movie1 = {}
    budget1 =0
    budget2=0
    budget3=0
    budget4=0
    budget5=0
    revenue1 =0
    revenue2 =0
    revenue3 =0
    revenue4 =0
    revenue5 =0
    for movie in moviesData:
        if movie['release_year'].isnumeric():
            if float(movie['release_year']) <= 1970:
                budget1 += float(movie['budget'])
                revenue1 += float(movie['revenue'])
            if float(movie['release_year']) >= 1971:
                if float(movie['release_year']) <=1981:
                    budget2 += float(movie['budget'])
                    revenue2 += float(movie['revenue'])
            if float(movie['release_year']) >= 1982:
                if float(movie['release_year']) <=1992:
                    budget3 += float(movie['budget'])
                    revenue3 += float(movie['revenue'])
            if float(movie['release_year']) >=1993:
                if float(movie['release_year']) <=2004:
                    budget4 += float(movie['budget'])
                    revenue4 += float(movie['revenue'])
            if float(movie['release_year']) >= 2005:
                budget5 += float(movie['budget'])
                revenue5 += float(movie['revenue'])
    year1 = "1960-1970"
    item1 = {"year":year1, "budget":budget1, "revenue":revenue1}
    response.append(item1)
    year2 = "1971-1981"
    item2 = {"year": year2, "budget": budget2, "revenue": revenue2}
    response.append(item2)
    year3 = "1982-1992"
    item3 = {"year": year3, "budget": budget3, "revenue": revenue3}
    response.append(item3)
    year4 = "1993-2003"
    item4 = {"year": year4, "budget": budget4, "revenue": revenue4}
    response.append(item4)
    year5 = "2004-2015"
    item5 = {"year": year5, "budget": budget5, "revenue": revenue5}
    response.append(item5)
    return response