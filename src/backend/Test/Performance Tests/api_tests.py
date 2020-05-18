import requests
import json

domains = ['localhost:5001','192.168.1.145:5000']
#domains = ['192.168.1.145:5000']
no_of_requests = 1

get_reqs =[
'http://domain//searchNumeric?search_field=id&search_inequality=0&search_query=12',
'http://domain//searchText?search_field=cast&search_query=chris',
'http://domain//searchFlopMovies?search_year=2015',
'http://domain//searchFlopMovies?search_year=',
'http://domain//highestGrossingMovie?search_year=2015',
'http://domain//aggregateMoviesBR' ,
'http://domain//analyticsGrenre?search_year=',
'http://domain//actorGenres?search_actor=Chris%20Pratt',
'http://domain//directorGenres?search_director=Woody%20Allen',
'http://domain//exportData?file_name=part6.csv',
'http://domain//importData?file_name=part2.csv'
]


post_reqs =['http://localhost:5000//insertData'
'http://localhost:5000//editData'
'http://localhost:5000//deleteMovie']

print(''.ljust(75),'UN-OPTIMIZED'.center(20), 'OPTIMIZED'.center(20))

for reqs in get_reqs:
    res = []
    for domain in domains:

        total_time = 0
        succesful_requests = 0
        for ite in range(no_of_requests):
            try:
                r = requests.get(reqs.replace('domain',domain))
                #print(reqs,r.status_code,'Time:',json.loads(r.text)['request_time'])
                total_time += json.loads(r.text)['request_time'] *1000
                succesful_requests += 1
            except:
                print('failure', reqs.replace('domain',domain))
        if succesful_requests != 0:
            res.append(round(total_time/succesful_requests,1))

    print(reqs.replace('http://domain//','').ljust(75), (str((res[0]))+' ms').center(20), (str(res[1])+' ms').center(20))