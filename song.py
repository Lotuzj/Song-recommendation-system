
from pandas import read_csv
from math import sqrt
import random

# getting csv file from internet
data_url = 'https://gist.githubusercontent.com/jackbandy/5cd988ab5c3d95b79219364dce7ee5ae/raw/731ecdbecc7b33030f23cd919e6067dfbaf42feb/song-ratings.csv'
ratings = read_csv(data_url, index_col=0)

# converting the column names to lowercase to avoid case sensitive problems
ratings.columns = ratings.columns.str.lower()

# getting user input song, of their liking (must be in csv file)
userinp = input("Enter your favorite song: ")

songseries = ratings[userinp.lower()]

# getting the highest rating of the song
songserieslist = songseries.to_list()
songserieslist.sort()

highest = songseries[-2]
songseriesdict = songseries.to_dict()

# finding user with highest rating of the song

userwhigh = None
for person in songseriesdict:
    if songseriesdict[person] == highest:
        userwhigh = person

# getting the songs users rated above their average ratings in history

usersongs = ratings.loc[userwhigh].to_dict()

topratedsongs = []

songsuserrated = list(usersongs.values())
avgrate = sum(songsuserrated) / len(songsuserrated)

for song in usersongs:
    if usersongs[song] >= avgrate:
        if song != userinp:
            topratedsongs.append(song)
# printing a random song from toprated songs by the similar liking music user
print("Recommended song:", random.choice(topratedsongs).title())