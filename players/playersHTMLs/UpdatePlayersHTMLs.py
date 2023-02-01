import requests

baseFolder = "/Users/jackgill/Desktop/CompProjProgram/players/playersHTMLs"

def downloadFile(url, outPutFileLocation):
    print ("Downloading - " + url)
    res = requests.get(url)
    # creates initially - overwrites with update HTML which is used for the 
    with open(outPutFileLocation, 'w') as f:
        f.write(res.text)

# URL for ROB KEARNEY
url  = "http://en.espn.co.uk/statsguru/rugby/player/15208.html?class=1;template=results;type=player"
outPutFileLocation = baseFolder + "/rKearney.html"

downloadFile(url,outPutFileLocation)

# URL for JONATHON SEXTON
url  = "http://en.espn.co.uk/statsguru/rugby/player/16004.html?class=1;template=results;type=player"
outPutFileLocation = baseFolder + "/jSexton.html"

downloadFile(url,outPutFileLocation)

# URL for CIAN HEALY
url  = "http://en.espn.co.uk/statsguru/rugby/player/15972.html?class=1;template=results;type=player"
outPutFileLocation = baseFolder + "/cHealy.html"

downloadFile(url,outPutFileLocation)

print("DOWNLOADS FINISHED")