import requests
from bs4 import BeautifulSoup
from pprint import pformat
from prettytable import PrettyTable
import re

def printResults():
    fileName = "/Users/jackgill/Desktop/CompProjProgram/comps/compsHTMLs/GuinessPro.html"
    soup = BeautifulSoup(open(fileName), 'html.parser')
    resultsArray = []
    # find the header for current squad
    h2 = soup.findAll("span",{"class": "mw-headline"},text=re.compile(r'####'))
    tables = soup.findAll("table")

    # data from first table
    # find the table within the header
    table = tables[0]

    # find the header row
    headers = table.findAll("th")

    # create header row array
    headerArray = []

    # iterate over the headers and each header text to header array
    for header in headers:
        headerArray.append(header.text)

    #add header array to table
    resultsArray.append(headerArray)

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
        resultsArray.append(rowArray)

    table1 = PrettyTable()
    table1.field_names = headerArray
    for row in resultsArray[1:-2]:
        table1.add_row(row)

    # find the table within the header
    table = tables[1]

    # find the header row
    headers = table.findAll("th")

    # create header row array
    headerArray = []
    resultsArray = []

    # iterate over the headers and each header text to header array
    for header in headers:
        headerArray.append(header.text)

    #add header array to table
    resultsArray.append(headerArray)

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
        resultsArray.append(rowArray)

    table2 = PrettyTable()
    table2.field_names = headerArray
    for row in resultsArray[1:-2]:
        table2.add_row(row)

    # dump the table
    return table1.get_string() + "\n\n\n" +  table2.get_string()

if __name__ == "__main__":
    print(printResults())