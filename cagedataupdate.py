import pickle
import csv
from pprint import PrettyPrinter
pp = PrettyPrinter()


f=open("cagewatch.txt")
cagewatched = []
for row in csv.reader(f):
    cagewatched.append(row)
print(cagewatched)
#with open('cagewatch.txt') as f:
#    watched = f.read().splitlines()




#
with open('cagemovies.pickle', 'rb') as handle:
    b = pickle.load(handle)

cagedict = b
#pp.pprint(b)
for movie in cagewatched:
    try:
        #print(movie[0])
        movieS = movie[0]
        cagedict[movieS]['watched'] = 'yes'
        cagedict[movieS]['watchdate'] = movie[1]
    except KeyError:
        print('KeyError' + movieS)

pp.pprint(cagedict)

with open('cagewatched.pickle', 'wb') as handle:
    pickle.dump(cagedict, handle, protocol=pickle.HIGHEST_PROTOCOL)
