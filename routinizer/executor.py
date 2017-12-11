import feedparser
import pickle as pk
import subprocess

def init():
    with open("../data/read_index", 'w') as f:
        pk.dump(0, f)

def loadData(linkLocation):
    data = feedparser.parse(linkLocation)
    read_index = int( pk.load( open("../data/read_index") ) )
    return (data, read_index)

def getNextLinkAndUpdateIndex(data, index):
    index += 1
    newLink = data.entries[index]['link']
    with open("../data/read_index", 'w') as f:
        pk.dump( index, f)

    return newLink

def executeRoutine():
    data, index = loadData("../data/paulgraham_essays.rss")
    link = getNextLinkAndUpdateIndex( data, index )

    print(link)
    subprocess.call(["xdg-open", link])
