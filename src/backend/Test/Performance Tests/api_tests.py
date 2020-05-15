import requests
import json

get_reqs =['http://localhost:5000//headers',
'http://localhost:5000//searchNumeric?search_field=id&search_query=12',
'http://localhost:5000//searchText?search_field=cast&search_query=chris',
'http://localhost:5000//searchFlopMovies?search_year=2015',
'http://localhost:5000//searchFlopMovies?search_year=',
'http://localhost:5000//highestGrossingMovie?search_year=2015',
'http://localhost:5000//aggregateMoviesBR' ,
'http://localhost:5000//analyticsGrenre?search_year=',
'http://localhost:5000//importData?file_name=part2.csv',
'http://localhost:5000//exportData?file_name=part6.csv',
'http://localhost:5000//popularityBubble',
'http://localhost:5000//exportList',
'http://localhost:5000//getTopDirectors',
'http://localhost:5000//getTopActors',
'http://localhost:5000//actorGenres?search_actor=Chris%20Pratt',
'http://localhost:5000//directorGenres?search_director=Woody%20Allen'

]

post_reqs =['http://localhost:5000//insertData'
'http://localhost:5000//editData'
'http://localhost:5000//deleteMovie']

for reqs in get_reqs:
    for ite in range(2):
        try:
            r = requests.get(reqs)
            print(reqs,r.status_code,'Time:',json.loads(r.text)['request_time'])
        except:
            print('failure', reqs)