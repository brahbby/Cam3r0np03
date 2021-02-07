import pickle
from pprint import PrettyPrinter
pp = PrettyPrinter()
import matplotlib.dates as dates
import matplotlib.pyplot as plt
from collections import Counter


#load dataset - run cagedata.py
with open('cagewatched.pickle', 'rb') as handle:
    b = pickle.load(handle)


count = 0
tmin = 0
timeRem = 0
valcount=0
burndata=[]
remcount=0
for movies in b:
    #print(movies)
    try:
        if b[movies]['watched'] == 'yes':
            print(b[movies]['Runtime'])
            time = int(b[movies]['Runtime'][:3])
            burndata.append([(b[movies]['watchdate']),int(b[movies]['Runtime'][:3]),b[movies]['Title']])
            tmin= tmin+time
    except KeyError:
        #print('notwatched')
        try:
            time = int(b[movies]['Runtime'][:3])
            timeRem= timeRem+time
            remcount = remcount+1
        except ValueError:
            valcount = valcount+1
        except KeyError:
            valcount = valcount+1
    #pp.pprint(movies)

print(tmin)
print(timeRem)
totalTime= tmin+timeRem
timeburn = totalTime
print(burndata)
burndata.sort(key = lambda burndata: burndata[0])
for movies in burndata:
    print(movies)
    timeburn = timeburn - movies[1]
    movies.append(timeburn)
    #print(timeburn)
print(burndata)
print(valcount)
print(tmin/(tmin+timeRem))
print(burndata[1][0],burndata[-1][0])

#need time remaining divded by averageoftmin
import datetime

def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)



daysWatching = days_between(burndata[0][0],burndata[-1][0])
print(len(burndata))
print(daysWatching)
#average time betweenz2 s1w movies
dayAvg = daysWatching/len(burndata)

#movies left divided by remaining timeRem
print(remcount)
print(timeburn)
avgLeft= timeburn/remcount

#average movie length

remBurndata = burndata
#loop and subtract avg time and add date
for movies in range(remcount):
    try:
        print(remBurndata[-1][0])
        date_1 = datetime.datetime.strptime(remBurndata[-1][0], "%Y-%m-%d")

        end_date = date_1 + datetime.timedelta(days=dayAvg)
        print(remBurndata[-1][0])
    except ValueError:
        try:
            date_1 = datetime.datetime.strptime(remBurndata[-1][0], "%Y-%m-%d %H:%M:%S.%f")
            end_date = date_1 + datetime.timedelta(days=dayAvg)
        except ValueError:
            try:
                date_1 = datetime.datetime.strptime(remBurndata[-1][0], "%Y-%m-%d %H:%M:%S")
                end_date = date_1 + datetime.timedelta(days=dayAvg)
            except ValueError:
                break
#    print(remBurndata[-1][0])
    timeburn = timeburn - avgLeft
    remBurndata.append([str(end_date),avgLeft,'Title',timeburn])
    #print(timeburn)
print(remBurndata)

for movies in remBurndata:
    #if movies[2] == 'Title':
    movies[0] = movies[0][:10]
    try:

        movies[0] = datetime.datetime.strptime(movies[0],"%Y-%m-%d %H:%M:%S")
    except:
        try:
            movies[0] = datetime.datetime.strptime(movies[0],"%Y-%m-%d %H:%M:%S.%f")
        except:
            movies[0] = datetime.datetime.strptime(movies[0],"%Y-%m-%d")

print(remBurndata)

chartdata = []
chartrem =[]
for movies in remBurndata:
    if movies[2] != 'Title':
        chartdata.append([movies[0],movies[3]])
    else:
        chartrem.append([movies[0],movies[3]])

x, y = zip(*chartdata)
x1, y1 = zip(*chartrem)


plt.fill_between(x, y)
plt.tight_layout()
plt.plot_date(x, y, linestyle ='solid')
plt.fill_between(x1, y1)
plt.tight_layout()
plt.plot_date(x1, y1, c='red', linestyle ='dashed')
plt.gcf().autofmt_xdate
plt.xticks(rotation=45)
plt.gcf().subplots_adjust(bottom=0.15)


plt.title("How'd it get burned(down)?!", fontsize=20)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Time Remaining in Goodspeeds (1.000000001 min)', fontsize=12)
plt.savefig('test.jpg',bbox_inches='tight')

plt.show()
# #pp.pprint(b)
# wGenre=[]
# uwGenre=[]
# valcount=0
# for movies in b:
#     #print(movies)
#     try:
#         if b[movies]['watched'] == 'yes':
#             genre = (b[movies]['Genre'])
#             wGenre.append(genre)
#     except ValueError:
#             valcount = valcount+1
#     except KeyError:
#         #print('notwatched')
#         try:
#             genre = (b[movies]['Genre'])
#             uwGenre.append(genre)
#         except ValueError:
#             valcount = valcount+1
#         except KeyError:
#             valcount = valcount+1
#
#
#
#
#
# print(wGenre)
# wlGenre=[]
# for genres in wGenre:
#     print(genres)
#     wlGenre.extend(genres.split(","))
# wlGenre = map(str.strip, wlGenre)
# print(wlGenre)
#
# uwlGenre=[]
# for genres in uwGenre:
#     print(genres)
#     uwlGenre.extend(genres.split(","))
# uwlGenre = map(str.strip, uwlGenre)
#
# print(uwlGenre)
#
# from collections import Counter
# import matplotlib.pyplot as plt
# import numpy as np
#
# counts = Counter(wlGenre)
# common = counts.most_common()
# labels = [item[0] for item in common]
# number = [item[1] for item in common]
# nbars = len(common)
#
# countsU = Counter(uwlGenre)
# commonU = countsU.most_common()
# labelsU = [item[0] for item in commonU]
# numberU = [item[1] for item in commonU]
# nbarsU = len(commonU)
#
#
# fig1, ax1 = plt.subplots()
# ax1.pie(number,  autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# ax1.set_title('Cage Watched Genres')
#
#
# ax1.legend(labels,
#           title="Genres",
#           loc="center left")
#
#           #bbox_to_anchor=(1, 0, 0.5, 1),
#          # bbox_inches='tight')
#
#
# fig1, ax2 = plt.subplots()
# ax2.pie(numberU, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax2.axis('equal')
# ax2.set_title('Cage UnWatched Genres')
# ax2.legend(labelsU,
#           title="Genres",
#           loc="center left")
#
# plt.tight_layout()
# plt.show()
#
# # plt.bar(np.arange(nbars), number, tick_label=labels)
# # plt.xticks(rotation=45)
# # plt.tight_layout()
# # plt.show()
