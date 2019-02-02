#!/usr/bin/python3

import bs4
import sys
import os



artist = sys.argv[1].replace(" ","_")
album = sys.argv[2].replace(" ", "_")



to_get = f"https://www.metal-archives.com/albums/{artist}/{album}"








# metal-archives does not like request.get
# So just used curl, because it werks


os.system("curl -s " + to_get + " > webpage.html")
open_file = open("webpage.html")


soup = bs4.BeautifulSoup(open_file ,"lxml")

# Wrap words is the metal archives css thingy for the album
elems = soup.select('.wrapWords')



split_songs = []
# This gets all the elemets(most are songs) and then finds the songs
# with the song.getText() It then splits the songs to get rid of the tabs
# then inserts them into the split_songs array

for song in elems:
    song = song.getText()
    song = song.split()
    split_songs.append(song)

# the split songs array is made up of multiple lists? (how!?)
# this takes that array and removes all the arry stuff from it
for song in split_songs:
    song = ' '.join(song)
    print(song)


os.remove("webpage.html")

