# ENGLAND
import requests
import re
from bs4 import BeautifulSoup
from pprint import pprint
from prettytable import PrettyTable

def printSquad():
    fileName = "/Users/jackgill/Desktop/CompProjProgram/intTeams/intTeamsHTMLs/ERU.html"

    soup = BeautifulSoup(open(fileName), 'html.parser')

    squadArray = []

    # find table
    tables = soup.findAll("table")
    table = tables[7]

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


        tds = row.findAll("td")
        for i, td in enumerate(tds):
            if i == 0:
                anchors = td.findAll('a')
                rowArray.append(anchors[0].getText())

            else: 
                rowArray.append(td.getText())
        
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