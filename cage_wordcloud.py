## Simple WordCloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from pprint import PrettyPrinter
import pickle
pp = PrettyPrinter()


text = 'all your base are belong to us all of your base base base'

with open('cagemovies.pickle', 'rb') as handle:
    b = pickle.load(handle)

pp.pprint(b)

kungstring =''
for i in b.keys():
    try:
        #print(b[i]['Plot'])
        kungstring =kungstring + ' ' + b[i]['Plot']
    except KeyError:
        continue

def generate_wordcloud(text): # optionally add: stopwords=STOPWORDS and change the arg below
    wordcloud = WordCloud(
                          width=800, height=400,
                          relative_scaling = 1.0,
                          stopwords = STOPWORDS#{'to', 'of'} # set or space-separated string
                          ).generate(text)

    fig = plt.figure(1, figsize=(8, 4))
    plt.axis('off')
    plt.imshow(wordcloud)
    plt.axis("off")
    ## Pick One:
    # plt.show()
    plt.savefig("WordCloud1.png")

generate_wordcloud(kungstring)
