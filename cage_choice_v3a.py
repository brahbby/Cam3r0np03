import random
import tkinter as tk
from PIL import ImageTk, Image
from pygame import mixer  # Load the popular external library
import random
import pickle
from pprint import PrettyPrinter
pp = PrettyPrinter()
import random
import time
#btn_text = tk.StringVar()





def cagepick():
    with open('cagewatched.pickle', 'rb') as handle:
        b = pickle.load(handle)
    #pp.pprint(b)
    watchscore =[]
    remscore =[]
    valcount=0
    uw=[]
    for movies in b:
        #print(movies)
        try:
            if b[movies]['watched'] == 'yes':

                watchscore.append(b[movies])
        except ValueError:
                valcount = valcount+1
        except KeyError:
            #print('notwatched')
            try:
                #remscore.append(b[movies])
                #print(b[movies])
                uw.append(b[movies]['Title'])
            except ValueError:
                valcount = valcount+1
            except KeyError:
                valcount = valcount+1


    moviepick =random.randint(0, len(uw))
    return(uw[moviepick])
    #print(remscore)


    with open('cagewatched.pickle', 'rb') as handle:
        b = pickle.load(handle)

    #pp.pprint(b)
    watchscore =[]
    remscore =[]
    valcount=0
    uw=[]
    for movies in b:
        #print(movies)
        try:
            if b[movies]['watched'] == 'yes':

                watchscore.append(b[movies])
        except ValueError:
                valcount = valcount+1
        except KeyError:
            #print('notwatched')
            try:
                #remscore.append(b[movies])
                #print(b[movies])
                uw.append(b[movies]['Title'])
            except ValueError:
                valcount = valcount+1
            except KeyError:
                valcount = valcount+1


    #print(uw)
    #print(len(uw))

    moviepick =random.randint(0, (len(uw)-1))
    print(moviepick)
    print(uw)
    return(uw[moviepick])

mixer.init()
#mixer.music.load('/home/brahbby/Documents/projects/cage//home/brahbby/Downloads/DIEEEEEEEEEEE.mp3')


window = tk.Tk()
window.title("Cage")
window.geometry("400x400")
window.configure(background='white')

def update_the_picture():
    #for fname in range(0,7):
    count =0
    num=random.randint(0, 11)
    soundnum = random.randint(0, 7)
    mixer.music.load("%d.wav" % (soundnum))
    mixer.music.play()
    print(len(images))
    while count < 20:
        num=random.randint(0, 11)
        print(num)
        w.configure(image = images[num])
        time.sleep(.1)
        count = count +1

    moviepick = cagepick()
    btn.configure(text=moviepick)
images=[]
for fname in range(1,13):
    img = ImageTk.PhotoImage(Image.open("cage%d.png" % (fname)))
    print(img)
    images.append(img)
print(images)

w = tk.Label(window, image = img)
w.pack(side = "bottom", fill = "both", expand = "yes")

btn = tk.Button(window, text="AM I GETTING THROUUUUGHHH TO YOU", command = update_the_picture)
btn.pack()

#update_the_picture()

window.mainloop()
