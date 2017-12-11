import feedparser
import pickle as pk
import subprocess

def init():
    pass
    #setReadIndex(0)

def setReadIndex(index):
    with open("../data/read_index", 'w') as f:
        pk.dump(index, f)

def loadData(linkLocation):
    data = feedparser.parse(linkLocation)
    read_index = int( pk.load( open("../data/read_index") ) )
    return (data, read_index)

def getNextLinkAndUpdateIndex(data, index):
    index += 1
    newLink = data.entries[index]['link']
    setReadIndex(index)

    return newLink

def executeRoutine():
    data, index = loadData("../data/paulgraham_essays.rss")
    link = getNextLinkAndUpdateIndex( data, index )

    print(link)
    # Open the link in a browser.
    subprocess.call(["xdg-open", link])
    # Show a notification.
    subprocess.call(["notify-send", "Routinizer", "Check you browser for" +
                    " today's essay."])
