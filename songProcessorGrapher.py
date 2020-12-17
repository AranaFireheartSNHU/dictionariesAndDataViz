#!/usr/bin/env python
__author__ = "Arana Fireheart"

from matplotlib.pyplot import rcdefaults, subplots, show
from numpy import array, arange
filename = "musicList.txt"


def processSong(songDictionary, nameOfArtist, nameOfSong, chartPosition):
    if '(' in nameOfSong:
        if nameOfSong.count('(') == 1:
            nameOfSong, junk = nameOfSong.split('(')
        else:
            nameOfSong = nameOfSong[:nameOfSong.index('(')]  # TODO Add featured artist to artist list
    elif '[' in nameOfSong:
        nameOfSong, junk = nameOfSong.split('[')
    if nameOfArtist in songDictionary:
        songDictionary[nameOfArtist].append([nameOfSong, chartPosition])
    else:
        songDictionary[nameOfArtist] = [[nameOfSong, chartPosition]]


def drawBarChart(appearances, graphTitle, axisLabels):
    xAxisLabel, yAxisLabel = axisLabels
    appearanceCounts = list(appearances.keys())
    namesLists = list(appearances.values())
    numberOfArtistsForCount = [len(namesList) for namesList in namesLists]
    appearanceCountsDictionary = dict(zip(appearanceCounts, numberOfArtistsForCount))
    appearanceCounts.sort()
    appearanceCountsPerCount = [appearanceCountsDictionary[position] for position in appearanceCounts]
    rcdefaults()
    frame, barChart = subplots()

    xData = array(appearanceCounts)
    yData = array(appearanceCountsPerCount)

    barChart.bar(xData, yData, align='center')
    barChart.set_xticks(xData)
    barChart.set_xticklabels(appearanceCounts)
    barChart.set_xlabel(xAxisLabel)
    barChart.set_ylabel(yAxisLabel)
    barChart.set_title(graphTitle)
    show()


def buildDictionaryFromFile(inputFilename):
    dataDictionary = {}
    with open(inputFilename, 'r') as musicInput:
        for lineNumber, line in enumerate(musicInput.readlines()):
            if len(line.strip()) > 0:
                artistName, songTitle = line.strip().split(' - ')
                if ', ' in artistName:
                    artistsNames = artistName.split(', ')
                    for artist in artistsNames:
                        processSong(dataDictionary, artist, songTitle, lineNumber + 1)
                        print(f"# {lineNumber} {artistName}")
                else:
                    processSong(dataDictionary, artistName, songTitle, lineNumber + 1)
                    print(f"# {lineNumber} {artistName}")
    return dataDictionary


billboardData = buildDictionaryFromFile(filename)   # build a dictionary from file data.


def buildAppearanceCounts():
    appearancesDictionary = {}
    for artist, songList in billboardData.items():
        appearanceCount = len(songList)
        try:
            appearancesDictionary[appearanceCount].append(artist)
        except KeyError:
            appearancesDictionary[appearanceCount] = [artist]
    return appearancesDictionary

appearances = buildAppearanceCounts()


chartTitle = "2020 Top Artists by track count"
axisTitles = ("Number of Appearances", "Artist Count")
drawBarChart(appearances, "2020 Top Artists by track count", axisTitles)

pass