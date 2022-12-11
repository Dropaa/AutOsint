import json
import os
import sys
from datetime import datetime
from time import sleep

import requests
import shodan
from dotenv import load_dotenv

load_dotenv()
URLSCAN_API_KEY = os.getenv("URLSCAN_API_KEY")

headers = {'API-Key': URLSCAN_API_KEY, 'Content-Type': 'application/json'}

def main():
    #apiUrl = getApiUrlURLScan()
    #sleep(10)
    #data = getDataURLScan(apiUrl)
    #readDataURLScan(data)
    ShodanTest()

def getDataURLScan(apiUrl):
    content = requests.get(apiUrl, {'Content-Type': 'application/json'})
    contentJson = json.loads(content.text)
    if ("status" in contentJson and contentJson.get("status") == 404):
        print("Url still not ready, retrying in 5 seconds...")
        sleep(5)
        return getDataURLScan(apiUrl)
    else:
        return contentJson

def readDataURLScan(data):
    for i in data["data"]["requests"]:
        url = i["response"]["response"]["url"]
        if url != "data:truncated":
            print(url + " ==> " + i["response"]["response"]["remoteIPAddress"])
            
    print("\nSUBDOMAIN : ")
    
    for i in data["lists"]["domains"]:
        print(i)
    
    print("\nCERTIFICATES : ")
    
    for i in data["lists"]["certificates"]:
        dateFrom = datetime.fromtimestamp(i["validFrom"])
        dateTo = datetime.fromtimestamp(i["validTo"])
        delta = dateTo - dateFrom
        print("Le certificat pour le sujet : " + i["subjectName"] + "a été accordé par : " + i["issuer"])
        print("Le certif est valable depuis : " + dateFrom.strftime("%d/%m/%Y") + " et s'arrête le : " + dateTo.strftime("%d/%m/%Y") + "soit un temps restant de : " + str(delta.days) + "  jours")
    

def getApiUrlURLScan():
    
    data = {"url": "https://esgi.fr", "visibility": "public"}
    response = requests.post(
        'https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))
    return response.json().get("api")

def ShodanTest():
    SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

    # The list of properties we want summary information on
    FACETS = [
        ('org', 10),
        ('domain', 10),
        ('port', 10),
        ('asn', 10),

        # We only care about the top 3 countries, this is how we let Shodan know to return 3 instead of the
        # default 5 for a facet. If you want to see more than 5, you could do ('country', 1000) for example
        # to see the top 1,000 countries for a search query.
        ('country', 5),
    ]

    FACET_TITLES = {
        'org': 'Top 10 Organizations',
        'domain': 'Top 10 Domains',
        'port': 'Top 10 Ports',
        'asn': 'Top 10 Autonomous Systems',
        'country': 'Top 5 Countries',
    }

    try:
        api = shodan.Shodan(SHODAN_API_KEY)
        query = "esgi"
        result = api.count(query, facets=FACETS)

        print ("Shodan Summary Information")
        print ("Query: " + query)
        print ("Total Results: " + str(result['total']) + "\n'")

        # Print the summary info from the facets
        for facet in result['facets']:
            print (str(FACET_TITLES[facet]))

            for term in result['facets'][facet]:
                print (str(term['value']) + ": " +  str(term['count']))

            # Print an empty line between summary info
            print ("")

    except Exception as e:
        print("Error: " + e)
        sys.exit(1)

if __name__ == "__main__":
    # read config file and loop where "use = yes"
        main()
