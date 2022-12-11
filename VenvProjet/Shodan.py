import os
import sys
from urllib.parse import urlparse

import shodan
from dotenv import load_dotenv
from OsintTool import OsintTool
from utils import write_file

load_dotenv()

SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

class Shodan(OsintTool):
    params = None
    output_data = []
    
    def __init__(self, params):
        self.params = params

    def run(self):
        FACETS = [
            ('org', 10),
            ('domain', 10),
            ('port', 10),
            ('asn', 10),
            ('country', 5),
        ]

        FACET_TITLES = {
            'org': '\nTop 10 Organizations',
            'domain': '\nTop 10 Domains',
            'port': '\nTop 10 Ports',
            'asn': '\nTop 10 Autonomous Systems',
            'country': '\nTop 5 Countries',
        }

        try:
            api = shodan.Shodan(SHODAN_API_KEY)
            query = urlparse(self.params["url"]).netloc.split(".")[1]
            result = api.count(query, facets=FACETS)
            self.output_data.append("Shodan Summary Information")
            self.output_data.append("Query: " + query)
            self.output_data.append("Total Results: " + str(result['total']))

            for facet in result['facets']:
                self.output_data.append(str(FACET_TITLES[facet]))

                for term in result['facets'][facet]:
                    self.output_data.append(str(term['value']) + ": " +  str(term['count']))
                    
            self.output()
        except Exception as e:
            print("Error: " + str(e))
            sys.exit(1)
            
            
    def output(self):
        write_file(urlparse(self.params["url"]).netloc , "shodan.txt", "\n".join(self.output_data))
  
  
    
  
  