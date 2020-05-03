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