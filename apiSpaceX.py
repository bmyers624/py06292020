#!/usr/bin/python3
"""
Author: RZFeeser
This program harvests SpaceX data avail from https://api.spacexdata.com/v3/cores using the Python Standard Library methods
"""

# using std library method for getting at API data
import urllib.request 
import json
import ssl

# GOBAL / CONSTANT of the API we want to lookup
SPACEXURI = "https://api.spacexdata.com/v3/cores"

def main():
    # create a urllib.request response object by sending an HTTP GET to SPACEXURI
    context = ssl._create_unverified_context()
    coreData = urllib.request.urlopen(SPACEXURI, context=context)

    # pull STRING data off of the 200 response (even tho it's JSON!)
    xString = coreData.read().decode()
    #print(type(xString))

    # convert STRING data into Python Lists and Dictionaries
    listOfCores = json.loads(xString)
    #print(type(listOfCores))

    for core in listOfCores:
        #print(core, end="\n\n")
        print(core['core_serial'])
        print(core['original_launch'], end="\n\n")
        missions = core['missions']
        if (len(missions) > 0 ):
            for mission in missions:
                print(f"- Flight {mission['flight']} in support of mission {mission['name']}")

        print("\n")

if __name__ == "__main__":
    main()
