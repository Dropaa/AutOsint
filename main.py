import json
import os
import sys
from time import sleep
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

headers = {'API-Key': API_KEY, 'Content-Type': 'application/json'}

def main():
    apiUrl = getApiUrl()
    sleep(10)
    data = getData(apiUrl)
    readData(data)

def getData(apiUrl):
    content = requests.get(apiUrl, {'Content-Type': 'application/json'})
    contentJson = json.loads(content.text)
    if ("status" in contentJson and contentJson.get("status") == 404):
        print("Url still not ready, retrying in 5 seconds...")
        sleep(5)
        return getData(apiUrl)
    else:
        return contentJson

def readData(data):
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
        #Essayer de fix le pb des str et int avec ce bout de code :
        #timestamp1 = 1609459200
        #timestamp2 = 1609865600
        #date1 = datetime.fromtimestamp(timestamp1)
        #date2 = datetime.fromtimestamp(timestamp2)
        #delta = date2 - date1
        #print(delta.days) # affiche : 4
                
        print("Le certificat pour le sujet : " + i["subjectName"] + "a été accordé par : " + i["issuer"])
        print("Le certif est valable depuis : " + dateFrom.strftime("%d/%m/%Y") + " et s'arrête le : " + dateTo.strftime("%d/%m/%Y"))
    

def getApiUrl():
    
    data = {"url": "https://esgi.fr", "visibility": "public"}
    response = requests.post(
        'https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))
    return response.json().get("api")

if __name__ == "__main__":
    print(sys.argv) # print args
    main()
