import requests
import re
import numpy
from bs4 import BeautifulSoup
from pprint import pformat
from prettytable import PrettyTable


def printStats():
    fileName = "/Users/jackgill/Desktop/CompProjProgram/players/playersHTMLs/jSexton.html"

    soup = BeautifulSoup(open(fileName), 'html.parser')

    playerArray = []

    # find the table
    tables = soup.findAll("table")
    table = tables[2]

    # find the header row
    headers = table.findAll("th")

    # create header row array
    headerArray = []

    # iterate over the headers and each header text to header array
    for header in headers:
        headerArray.append(header.text)

    #add header array to table
    playerArray.append(headerArray)

    # find all rows in the table
    rows = table.findAll("tr")

    # iterate over rows - skipping first row because it is the header
    for row in rows[1:]:
        # find all anchor tags in the row
        tds = row.findAll("td")
        # create row array
        rowArray = []
        # iterate over all anchors
        for td in tds:
            # skip the img anchor - not needed
            if len(td.text) > 0 :
                # add the anchor text to the row array
                rowArray.append(td.text)
        
        # adding row arry to the table array
        playerArray.append(rowArray)

# dump the table
    transposedTable = numpy.transpose(playerArray).tolist()[1:-1]
    table = PrettyTable()
    table.field_names = transposedTable[0]
    print (transposedTable[0])
    for row in transposedTable[1:]:
        table.add_row(row)

    return table.get_string()

if __name__ == "__main__":
    print(printStats())