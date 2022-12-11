import json
import os
from datetime import datetime
from time import sleep
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv
from OsintTool import OsintTool
from utils import write_file

load_dotenv()

API_KEY = os.getenv("URLSCAN_API_KEY")

class UrlScan(OsintTool):
    params = None
    output_data = []
    
    def __init__(self, params):	
        self.params = params

    def run(self):
        apiUrl = self.get_api_url()
        sleep(10)
        data = self.get_data_from_url(apiUrl)
        self.read_data(data)
        self.output()
    
    def get_data_from_url(self, url):
        content = requests.get(url, {'Content-Type': 'application/json'})
        contentJson = json.loads(content.text)
        if ("status" in contentJson and contentJson.get("status") == 404):
            print("Url still not ready, retrying in 5 seconds...")
            sleep(5)
            return self.get_data_from_url(url)
        else:
            return contentJson
    
    def get_api_url(self):
        response = requests.post('https://urlscan.io/api/v1/scan/', headers={'API-Key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps({"url": self.params["url"], "visibility": "public"}))
        return response.json().get("api")

    def read_data(self, data):
        self.output_data.append("URL ==> RemoteIPAdress: \n")
        for i in data["data"]["requests"]:
            url = i["response"]["response"]["url"]
            if url != "data:truncated":
                self.output_data.append(url + " ==> " + i["response"]["response"]["remoteIPAddress"])
                
        self.output_data.append("\n-----------------------------------------\n")
        self.output_data.append("SUBDOMAINS: \n")
        
        for i in data["lists"]["domains"]:
            self.output_data.append(i)
            
        self.output_data.append("\n----------------------------------------\n")
        self.output_data.append("CERTIFICATES : \n")
        
        for i in data["lists"]["certificates"]:
            dateFrom = datetime.fromtimestamp(i["validFrom"])
            dateTo = datetime.fromtimestamp(i["validTo"])
            delta = dateTo - dateFrom
            self.output_data.append("Le certificat pour le sujet : " + i["subjectName"] + "a été accordé par : " + i["issuer"])
            self.output_data.append("Le certif est valable depuis : " + dateFrom.strftime("%d/%m/%Y") + " et s'arrête le : " + dateTo.strftime("%d/%m/%Y") + "soit un temps restant de : " + str(delta.days) + " jours")
            
    def output(self):
        write_file(urlparse(self.params["url"]).netloc ,self.params["output"], "\n".join(self.output_data))