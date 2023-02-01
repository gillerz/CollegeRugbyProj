import requests


baseFolder = "/Users/jackgill/Desktop/CompProjProgram/intTeams/intTeamsHTMLs"

def downloadFile(url, outPutFileLocation):
    print ("Downloading - " + url)
    res = requests.get(url)
    # creates initially - overwrites with update HTML which is used for the 
    with open(outPutFileLocation, 'w') as f:
        f.write(res.text)

# URL for IRELAND
url  = "https://en.wikipedia.org/wiki/Ireland_national_rugby_union_team"
outPutFileLocation = baseFolder + "/IRFU.html"

downloadFile(url,outPutFileLocation)

# URL for ENGLAND
url  = "https://en.wikipedia.org/wiki/England_national_rugby_union_team"
outPutFileLocation = baseFolder + "/ERU.html"

downloadFile(url,outPutFileLocation)

print("DOWNLOADS FINISHED")


