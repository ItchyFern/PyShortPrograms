# used with the csv files mentioned...
# This program simply searches a database filled with names of cities
# and their corresponding postal codes, then matches it with a file full
# of postal codes and no city names. This was used because a exported
# copy of a client list did not include which city the client was from

import sys
import os
import csv
from bs4 import BeautifulSoup
import requests



def main(postalCode):
    inputfile = csv.DictReader(open("file.csv"))
    postalfile = csv.DictReader(open("jcsv.csv"))
    lookuparray = []
    postalarray = []
    count = 0
    for row in inputfile:
        lookuparray.append(row)
    for row in postalfile:
        for code in lookuparray:
            if row['CZIP'][:3]==code['Postal Code']:
                count+=1
                print(row['CZIP'] + ": " + code["Place Name"])
                break








if __name__ == '__main__':
    main('k0l2h0')
