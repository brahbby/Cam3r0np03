import requests
from pprint import PrettyPrinter
import pickle





pp = PrettyPrinter()

with open('cagemovies.txt') as f:
    lines = f.read().splitlines()
print(lines)
apiKey = '6aec35b7&'
#Fetch Movie Data with Full Plot
cagedict={}
data_URL = 'http://www.omdbapi.com/?apikey='+apiKey
year = ''
for movies in lines:
    params = {
        't':movies,
        'type':'movie',
        'y':year,
        'plot':'full'
        }
    response = requests.get(data_URL,params=params).json()
    cagedict[movies]=response
    pp.pprint(cagedict)


with open('cagemovies.pickle', 'wb') as handle:
    pickle.dump(cagedict, handle, protocol=pickle.HIGHEST_PROTOCOL)
