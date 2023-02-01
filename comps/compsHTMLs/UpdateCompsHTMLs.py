import requests


baseFolder = "/Users/jackgill/Desktop/CompProjProgram/comps/compsHTMLs"

def downloadFile(url, outPutFileLocation):
    print ("Downloading - " + url)
    res = requests.get(url)
    # creates initially - overwrites with update HTML which is used for the 
    with open(outPutFileLocation, 'w') as f:
        f.write(res.text)

# URL for Guiness Pro Series
url  = "http://www.bbc.co.uk/sport/rugby-union/pro12/table"
outPutFileLocation = baseFolder + "/GuinessPro.html"

downloadFile(url,outPutFileLocation)


print("DOWNLOADS FINISHED")
