import requests

baseFolder = "/Users/jackgill/Desktop/CompProjProgram/clubTeams/clubHTMLs"

def downloadFile(url, outPutFileLocation):
    print ("Downloading - " + url)
    res = requests.get(url)
    # creates initially - overwrites with update HTML which is used for the 
    with open(outPutFileLocation, 'w') as f:
        f.write(res.text)

# URL for Leinster 
url  = "https://en.wikipedia.org/wiki/Leinster_Rugby"
outPutFileLocation = baseFolder + "/Leinster.html"

downloadFile(url,outPutFileLocation)

# URL for Ulster page
url  = "https://en.wikipedia.org/wiki/Ulster_Rugby"
outPutFileLocation = baseFolder + "/Ulster.html"

downloadFile(url,outPutFileLocation)

# URL for Connacht page
url  = "https://en.wikipedia.org/wiki/Connacht_Rugby"
outPutFileLocation = baseFolder + "/Connacht.html"

downloadFile(url,outPutFileLocation)

# URL for Munster page
url  = "https://en.wikipedia.org/wiki/Munster_Rugby"
outPutFileLocation = baseFolder + "/Munster.html"

downloadFile(url,outPutFileLocation)

print("DOWNLOADS FINISHED")
