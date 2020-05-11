###
    ##
###
def moviesAggregate(moviesData):
    response =[]
    myMin =1960
    myMax = 2015
    budget1 =0
    budget2=0
    budget3=0
    budget4=0
    budget5=0
    budget6=0
    budget7=0
    budget8=0
    revenue1 =0
    revenue2 =0
    revenue3 =0
    revenue4 =0
    revenue5 =0
    revenue6 = 0
    revenue7 = 0
    revenue8 = 0

    for movie in moviesData:
        if movie['release_year'].isnumeric():
            if float(movie['release_year']) <= 1966:
                budget1 += float(movie['budget'])
                revenue1 += float(movie['revenue'])
            if float(movie['release_year']) >= 1967:
                if float(movie['release_year']) <=1973:
                    budget2 += float(movie['budget'])
                    revenue2 += float(movie['revenue'])
            if float(movie['release_year']) >= 1974:
                if float(movie['release_year']) <=1980:
                    budget3 += float(movie['budget'])
                    revenue3 += float(movie['revenue'])
            if float(movie['release_year']) >=1981:
                if float(movie['release_year']) <=1987:
                    budget4 += float(movie['budget'])
                    revenue4 += float(movie['revenue'])
            if float(movie['release_year']) >=1988:
                if float(movie['release_year']) <=1994:
                    budget5 += float(movie['budget'])
                    revenue5 += float(movie['revenue'])
            if float(movie['release_year']) >=1995:
                if float(movie['release_year']) <=2001:
                    budget6 += float(movie['budget'])
                    revenue6 += float(movie['revenue'])
            if float(movie['release_year']) >=2002:
                if float(movie['release_year']) <=2008:
                    budget7 += float(movie['budget'])
                    revenue7 += float(movie['revenue'])
            if float(movie['release_year']) >= 2009:
                if float(movie['release_year'])>2015:
                    myMax = float(movie['release_year'])
                budget8 += float(movie['budget'])
                revenue8 += float(movie['revenue'])
    year1 = "1960-1966"
    item1 = {"year":year1, "budget":budget1, "revenue":revenue1}
    response.append(item1)
    year2 = "1967-1973"
    item2 = {"year": year2, "budget": budget2, "revenue": revenue2}
    response.append(item2)
    year3 = "1974-1980"
    item3 = {"year": year3, "budget": budget3, "revenue": revenue3}
    response.append(item3)
    year4 = "1981-1987"
    item4 = {"year": year4, "budget": budget4, "revenue": revenue4}
    response.append(item4)
    year5 = "1988-1994"
    item5 = {"year": year5, "budget": budget5, "revenue": revenue5}
    response.append(item5)
    year6 = "1995-2001"
    item6 = {"year": year6, "budget": budget6, "revenue": revenue6}
    response.append(item6)
    year7 = "2002-2008"
    item7 = {"year": year7, "budget": budget7, "revenue": revenue7}
    response.append(item7)
    year8 = "2009-"+str(myMax)
    item8 = {"year": year8, "budget": budget8, "revenue": revenue8}
    response.append(item8)
    return response


###
    ## searchFlopMovies function returns list of all movies whose budget is more than revenue
###
def searchFlopMovies(year, moviesData):
    responseObject = []
    if year == '':
        minD=0
        item ={}
        for movie in moviesData:
            if float(movie['budget']) > float(movie['revenue']):
                if float(movie['revenue'])>0:
                    diff = float(movie['budget']) - float(movie['revenue'])
                    if diff > minD:
                            minD = diff
                            item = movie

        item['loss'] = minD
        responseObject.append(item)
        return responseObject
    else:
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
    responseObject = []
    _grossIncome = 0
    maxGross = 0
    if year == '':
        item ={}
        for movie in moviesData:
            if float(movie['budget']) < float(movie['revenue']):
                if float(movie['budget'])>0:
                    diff = float(movie['revenue']) - float(movie['budget'])
                    if diff > maxGross:
                            maxGross = diff
                            item = movie
        item['profit'] = maxGross
        responseObject.append(item)
        return responseObject

    else:
        for movie in moviesData:
            if movie['release_year'] == year:
                if float(movie['budget']) < float(movie['revenue']):
                    if float(movie['budget']) != 0:
                        diff = float(movie['revenue']) - float(movie['budget'])
                        movie['profit'] = diff
                        responseObject.append(movie)

        responseObject = sorted(responseObject, key=lambda i: i['profit'], reverse=True)
        responseObject = responseObject[:10]
        return responseObject

####
def analyticsGrenre(year, moviesData):
    responseObject =[]
    action = 0
    thriller =0
    adventure =0
    fiction =0
    drama =0
    fantasy =0
    crime =0
    comedy =0
    animation =0
    family =0
    mystery =0
    romance =0

    if year=='':
        for movie in moviesData:
            if movie['revenue'].isdigit():
                if movie['budget'].isdigit():
                    if 'Action' in movie['genres']:
                        action = action + (float(movie['revenue'])-float(movie['budget']))
                    if 'Thriller' in movie['genres']:
                        thriller += (float(movie['revenue'])-float(movie['budget']))
                    if 'Adventure' in movie['genres']:
                        adventure += (float(movie['revenue'])-float(movie['budget']))
                    if 'Science Fiction' in movie['genres']:
                        fiction += (float(movie['revenue'])-float(movie['budget']))
                    if 'Drama' in movie['genres']:
                        drama += (float(movie['revenue'])-float(movie['budget']))
                    if 'Fantasy' in movie['genres']:
                        fantasy += (float(movie['revenue'])-float(movie['budget']))
                    if 'Crime' in movie['genres']:
                        crime += (float(movie['revenue'])-float(movie['budget']))
                    if 'Comedy' in movie['genres']:
                        comedy += (float(movie['revenue'])-float(movie['budget']))
                    if 'Animation' in movie['genres']:
                        animation += (float(movie['revenue'])-float(movie['budget']))
                    if 'Family' in movie['genres']:
                        family += (float(movie['revenue'])-float(movie['budget']))
                    if 'Mystery' in movie['genres']:
                        mystery += (float(movie['revenue'])-float(movie['budget']))
                    if 'Romance' in movie['genres']:
                        romance += (float(movie['revenue'])-float(movie['budget']))
    else:
        for movie in moviesData:
            if movie['release_year'] == year:
                if movie['revenue'].isdigit():
                    if movie['budget'].isdigit():
                        if 'Action' in movie['genres']:
                            action = action + (float(movie['revenue']) - float(movie['budget']))
                        if 'Thriller' in movie['genres']:
                            thriller += (float(movie['revenue']) - float(movie['budget']))
                        if 'Adventure' in movie['genres']:
                            adventure += (float(movie['revenue']) - float(movie['budget']))
                        if 'Science Fiction' in movie['genres']:
                            fiction += (float(movie['revenue']) - float(movie['budget']))
                        if 'Drama' in movie['genres']:
                            drama += (float(movie['revenue']) - float(movie['budget']))
                        if 'Fantasy' in movie['genres']:
                            fantasy += (float(movie['revenue']) - float(movie['budget']))
                        if 'Crime' in movie['genres']:
                            crime += (float(movie['revenue'])- float(movie['budget']))
                        if 'Comedy' in movie['genres']:
                            comedy += (float(movie['revenue']) - float(movie['budget']))
                        if 'Animation' in movie['genres']:
                            animation += (float(movie['revenue']) - float(movie['budget']))
                        if 'Family' in movie['genres']:
                            family += (float(movie['revenue']) - float(movie['budget']))
                        if 'Mystery' in movie['genres']:
                            mystery += (float(movie['revenue']) - float(movie['budget']))
                        if 'Romance' in movie['genres']:
                            romance += (float(movie['revenue']) - float(movie['budget']))

    responseObject.append({"genre_type": "Action", "total_amt":action})
    responseObject.append({"genre_type": "Thriller", "total_amt":thriller})
    responseObject.append({"genre_type": "Adventure", "total_amt": adventure})
    responseObject.append({"genre_type": "Fiction", "total_amt": fiction})
    responseObject.append({"genre_type": "Drama", "total_amt": drama})
    responseObject.append({"genre_type": "Fantasy", "total_amt": fantasy})
    responseObject.append({"genre_type": "Crime", "total_amt": crime})
    responseObject.append({"genre_type": "Comedy", "total_amt": comedy})
    responseObject.append({"genre_type": "Animation", "total_amt": animation})
    responseObject.append({"genre_type": "Family", "total_amt": family})
    responseObject.append({"genre_type": "Mystery", "total_amt": mystery})
    responseObject.append({"genre_type": "Romance", "total_amt": romance})
    responseObject = sorted(responseObject, key=lambda i: i['total_amt'], reverse=True)
    record = {"RECORDS":responseObject}
    return record


def actorGenres(actorName, moviesData):
    responseObject = []
    action = 0
    thriller = 0
    adventure = 0
    fiction = 0
    drama = 0
    fantasy = 0
    crime = 0
    comedy = 0
    animation = 0
    family = 0
    mystery = 0
    romance = 0

    for movie in moviesData:
        if actorName in movie['cast']:
            if 'Action' in movie['genres']:
                action += 1
            if 'Thriller' in movie['genres']:
                thriller += 1
            if 'Adventure' in movie['genres']:
                adventure += 1
            if 'Science Fiction' in movie['genres']:
                fiction += 1
            if 'Drama' in movie['genres']:
                drama += 1
            if 'Fantasy' in movie['genres']:
                fantasy += 1
            if 'Crime' in movie['genres']:
                crime += 1
            if 'Comedy' in movie['genres']:
                comedy += 1
            if 'Animation' in movie['genres']:
                animation += 1
            if 'Family' in movie['genres']:
                family += 1
            if 'Mystery' in movie['genres']:
                mystery += 1
            if 'Romance' in movie['genres']:
                romance += 1

    responseObject.append({"genre_type": "Action", "total": action})
    responseObject.append({"genre_type": "Thriller", "total": thriller})
    responseObject.append({"genre_type": "Adventure", "total": adventure})
    responseObject.append({"genre_type": "Fiction", "total": fiction})
    responseObject.append({"genre_type": "Drama", "total": drama})
    responseObject.append({"genre_type": "Fantasy", "total": fantasy})
    responseObject.append({"genre_type": "Crime", "total": crime})
    responseObject.append({"genre_type": "Comedy", "total": comedy})
    responseObject.append({"genre_type": "Animation", "total": animation})
    responseObject.append({"genre_type": "Family", "total": family})
    responseObject.append({"genre_type": "Mystery", "total": mystery})
    responseObject.append({"genre_type": "Romance", "total": romance})
    responseObject = sorted(responseObject, key=lambda i: i['total'], reverse=True)
    record = {"RECORDS": responseObject}
    return record

def directorGenres(dirName, moviesData):
    responseObject = []
    action = 0
    thriller = 0
    adventure = 0
    fiction = 0
    drama = 0
    fantasy = 0
    crime = 0
    comedy = 0
    animation = 0
    family = 0
    mystery = 0
    romance = 0

    for movie in moviesData:
        if dirName == movie['director']:
            if 'Action' in movie['genres']:
                action += 1
            if 'Thriller' in movie['genres']:
                thriller += 1
            if 'Adventure' in movie['genres']:
                adventure += 1
            if 'Science Fiction' in movie['genres']:
                fiction += 1
            if 'Drama' in movie['genres']:
                drama += 1
            if 'Fantasy' in movie['genres']:
                fantasy += 1
            if 'Crime' in movie['genres']:
                crime += 1
            if 'Comedy' in movie['genres']:
                comedy += 1
            if 'Animation' in movie['genres']:
                animation += 1
            if 'Family' in movie['genres']:
                family += 1
            if 'Mystery' in movie['genres']:
                mystery += 1
            if 'Romance' in movie['genres']:
                romance += 1

    responseObject.append({"genre_type": "Action", "total": action})
    responseObject.append({"genre_type": "Thriller", "total": thriller})
    responseObject.append({"genre_type": "Adventure", "total": adventure})
    responseObject.append({"genre_type": "Fiction", "total": fiction})
    responseObject.append({"genre_type": "Drama", "total": drama})
    responseObject.append({"genre_type": "Fantasy", "total": fantasy})
    responseObject.append({"genre_type": "Crime", "total": crime})
    responseObject.append({"genre_type": "Comedy", "total": comedy})
    responseObject.append({"genre_type": "Animation", "total": animation})
    responseObject.append({"genre_type": "Family", "total": family})
    responseObject.append({"genre_type": "Mystery", "total": mystery})
    responseObject.append({"genre_type": "Romance", "total": romance})
    responseObject = sorted(responseObject, key=lambda i: i['total'], reverse=True)
    record = {"RECORDS": responseObject}
    return record

def analyticsPopularity(year,moviesData):

    return_object = []

    for movie in moviesData:

        if movie['release_year'] == year and len(movie['genres']) > 0:
            return_object.append({'name':movie['original_title'] , 'title': movie['original_title'], 'group': movie['genres'][0], 'value':movie['popularity']})

    return return_object

