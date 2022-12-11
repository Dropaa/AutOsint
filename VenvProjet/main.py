import os
import sys

import shodan
from dotenv import load_dotenv
from OsintToolBuilder import OsintToolBuilder


def ShodanTest():
    SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

    # The list of properties we want summary information on
    FACETS = [
        'org',
        'domain',
        'port',
        'asn',

        # We only care about the top 3 countries, this is how we let Shodan know to return 3 instead of the
        # default 5 for a facet. If you want to see more than 5, you could do ('country', 1000) for example
        # to see the top 1,000 countries for a search query.
        ('country', 3),
    ]

    FACET_TITLES = {
        'org': 'Top 5 Organizations',
        'domain': 'Top 5 Domains',
        'port': 'Top 5 Ports',
        'asn': 'Top 5 Autonomous Systems',
        'country': 'Top 3 Countries',
    }

    try:
        api = shodan.Shodan(SHODAN_API_KEY)
        query = "https://esgi.fr"
        result = api.count(query, facets=FACETS)

        print ("Shodan Summary Information")
        print ("Query: " + query)
        print ("Total Results: " + result['total'] + "\n'")

        # Print the summary info from the facets
        for facet in result['facets']:
            print (FACET_TITLES[facet])

            for term in result['facets'][facet]:
                print (term['value'] + ": " +  term['count'])

            # Print an empty line between summary info
            print ("")

    except Exception as e:
        print("Error: " + e)
        sys.exit(1)

if __name__ == "__main__":
    # read config file and loop where "use = yes"
    tool = OsintToolBuilder.getTool("urlscan", {"url": "https://esgi.fr", "output": "urlscan.txt"})
    tool.run()
    