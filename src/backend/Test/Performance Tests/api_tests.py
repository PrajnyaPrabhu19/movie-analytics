import requests
import json

domains = ['localhost:5000',]
no_of_requests = 1

get_reqs =[
'http://domain//searchNumeric?search_field=id&search_query=12',
'http://domain//searchText?search_field=cast&search_query=chris',
'http://domain//searchFlopMovies?search_year=2015',
'http://domain//searchFlopMovies?search_year=',
'http://domain//highestGrossingMovie?search_year=2015',
'http://domain//aggregateMoviesBR' ,
'http://domain//analyticsGrenre?search_year=',
'http://domain//importData?file_name=part2.csv',
'http://domain//exportData?file_name=part6.csv',
'http://domain//exportList',
'http://domain//getTopDirectors',
'http://domain//getTopActors',
'http://domain//actorGenres?search_actor=Chris%20Pratt',
'http://domain//directorGenres?search_director=Woody%20Allen'

]


post_reqs =['http://localhost:5000//insertData'
'http://localhost:5000//editData'
'http://localhost:5000//deleteMovie']


for domain in domains:
    for reqs in get_reqs:
        reqs = reqs.replace('domain',domain)
        total_time = 0
        succesful_requests = 0
        for ite in range(no_of_requests):
            try:
                r = requests.get(reqs)
                #print(reqs,r.status_code,'Time:',json.loads(r.text)['request_time'])
                total_time += json.loads(r.text)['request_time'] *1000
                succesful_requests += 1
            except:
                print('failure', reqs)
        if succesful_requests != 0:
            print(reqs,' AVG TIME', total_time/succesful_requests , 'ms')