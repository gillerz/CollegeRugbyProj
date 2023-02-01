import requests
import re
from bs4 import BeautifulSoup
from pprint import pformat
from prettytable import PrettyTable

def printSquad():
    fileName = "/Users/jackgill/Desktop/CompProjProgram/clubTeams/clubHTMLs/Connacht.html"

    soup = BeautifulSoup(open(fileName), 'html.parser')

    squadArray = []

    # find the header for current squad
    tables = soup.findAll("table")

    # find the table within the header
    table = tables[6]

    # find the header row
    headers = table.findAll("th")

    # create header row array
    headerArray = []

    # iterate over the headers and each header text to header array
    for header in headers:
        headerArray.append(header.text)

    #add header array to table
    squadArray.append(headerArray)

    # find all rows in the table
    rows = table.findAll("tr")

    # iterate over rows - skipping first row because it is the header
    for row in rows[1:]:
        # find all anchor tags in the row
        allAs = row.findAll("a")
        # create row array
        rowArray = []
        # iterate over all anchors
        for a in allAs:
            # skip the img anchor - not needed
            if len(a.text) > 1 :
                # add the anchor text to the row array
                rowArray.append(a.text)
        
        # adding row arry to the table array
        squadArray.append(rowArray)

    # now get second table
    table = tables[7]

     # find all rows in the table
    rows = table.findAll("tr")

    # iterate over rows - skipping first row because it is the header
    for row in rows[1:]:
        # find all anchor tags in the row
        allAs = row.findAll("a")
        # create row array
        rowArray = []
        # iterate over all anchors
        for a in allAs:
            # skip the img anchor - not needed
            if len(a.text) > 1 :
                # add the anchor text to the row array
                rowArray.append(a.text)
        
        # adding row arry to the table array
        squadArray.append(rowArray)

    table = PrettyTable()
    table.field_names = headerArray
    for row in squadArray[1:]:
        table.add_row(row)

    # dump the table
    return table.get_string()

# un-comment/comment the following to test in terminal
if __name__ == "__main__":
    print (printSquad())

