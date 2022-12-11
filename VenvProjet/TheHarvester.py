import os
from urllib.parse import urlparse

from OsintTool import OsintTool


class TheHarvester(OsintTool):
    params = None
    def __init__(self, params):
        self.params = params
        pass
        
    def run(self):
        query = urlparse(self.params["url"]).netloc
        output = os.system("theHarvester -d " + query + " -b all > logs/" + query + ".theHarvester.txt")

    def output(self):
        return super().output()
    