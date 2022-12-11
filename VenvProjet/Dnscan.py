import os
from urllib.parse import urlparse

from OsintTool import OsintTool


class Dnscan(OsintTool):
    params = None
    def __init__(self, params):
        self.params = params
        pass
        
    def run(self):
        query = urlparse(self.params["url"]).netloc
        os.system("python3 ../dnscan/dnscan.py -n -d  " + query + " > ../VenvProjet/logs/" + query + ".dnscan.txt")

    def output(self):
        return super().output()