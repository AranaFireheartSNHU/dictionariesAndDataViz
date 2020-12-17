#!/usr/bin/env python
__author__ = "Arana Fireheart"

filename = "musicList.txt"

billboardData = {}
appearances ={}

def processSong(nameOfArtist, nameOfSong, chartPosition):
    if '(' in nameOfSong:
        if nameOfSong.count('(') == 1:
            nameOfSong, junk = nameOfSong.split('(')
        else:
            nameOfSong = nameOfSong[:nameOfSong.index('(')]  # TODO Add featured artist to artist list
    elif '[' in nameOfSong:
        nameOfSong, junk = nameOfSong.split('[')
    if nameOfArtist in billboardData:
        billboardData[nameOfArtist].append([nameOfSong, chartPosition])
    else:
        billboardData[nameOfArtist] = [[nameOfSong, chartPosition]]


with open(filename, 'r') as musicInput:
    for lineNumber, line in enumerate(musicInput.readlines()):
        if len(line.strip()) > 0:
            artistName, songTitle = line.strip().split(' - ')
            if ', ' in artistName:
                artistsNames = artistName.split(', ')
                for artist in artistsNames:
                    processSong(artist, songTitle, lineNumber + 1)
                    print(f"# {lineNumber} {artistName}")
            else:
                processSong(artistName, songTitle, lineNumber + 1)
                print(f"# {lineNumber} {artistName}")

for artist, songList in billboardData.items():
    appearanceCount = len(songList)
    try:
        appearances[appearanceCount].append(artist)
    except KeyError:
        appearances[appearanceCount] = [artist]

pass