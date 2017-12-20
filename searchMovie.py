# could do this import argparse

import sys
import urllib.request
import json

#This require Python 3. I used Python3.6 while I was implementing this function
#This function will take one user command line argument and send a request using HTTP link
#Once it receive response, it will process as Json data
#It will store number of pages that it need to go through and number of expected result
#Base on number of pages, it will go through one by one in for loop
#During each pages, it will look for keyword 'Title' and store them to list
#Then I check whether the list is empty or whether number of expected and actual result is the same or not
#After that I used print using sorted() apit cuz I am not sure whether we want to permentally rearrange the whole list or not
#I could add argparser for nicer userfriendly command line support

def main():
    movieName = None
    httpLink = "https://jsonmock.hackerrank.com/api/movies/search/?Title="
    respData = None
    jsonData = None
    numberPages = 0
    movieList = []
    expectedTitleNumber = 0

    if len( sys.argv ) == 2:
        movieName = sys.argv[1]
    elif len ( sys.argv) < 2 :
        print("Require at least one input")
        sys.exit(1)
    else :
        print("Warnning !!! Only support ONE argument currently. Will ignore the rest")
        movieName = sys.argv[1]

    httpLink = httpLink+movieName
    respData = urllib.request.urlopen(httpLink).read()
    respDataJson = json.loads(respData)

    numberPages = respDataJson['total_pages']
    expectedTitleNumber = respDataJson['total']

    for i in range( 1, numberPages+1):
        query = httpLink + "&page="+ str(i)
        respQuery = urllib.request.urlopen(query).read()
        respQueryJson = json.loads(respQuery)
        for j in respQueryJson['data']:
            if 'Title' not in j:
                print("Warnning!!! Title key is missing in ", j)
                continue
            movieList.append(j['Title'])

    if len(movieList) == 0 :
        print("Couldn't find any movie Title with subString = ", movieName)
    elif len(movieList) != expectedTitleNumber:
        print("Warnning!!! Expected Movie Title is : ", expectedTitleNumber, " But only found : ", len(movieList))
    else :
        print("##### Found ",  len(movieList), " Movie Titles #####")
        for i in sorted(movieList):
            print(i)


if __name__ == "__main__":
    main()