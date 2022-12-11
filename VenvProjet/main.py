import argparse
import json
import re
import sys

from OsintToolBuilder import OsintToolBuilder


def get_active_tools():
    file = open("conf.json", "r")
    data = json.load(file)
    file.close()
    return [tool for tool in data["activeTools"] if data["activeTools"][tool] == True]

if __name__ == "__main__":
    # read config file and loop where "use = yes"
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--help", "-h", action="help", help="Affiche l'aide")
    parser.add_argument("--domain", "-d", help="Inserer le domaine à analyser", required=True)
    args = parser.parse_args()
    
    with open("tlds.txt") as file:
        lines = [line.rstrip() for line in file]
        tld = "|".join(lines)
        if(re.match("^(https|http|ftp|sftp):\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.(" + tld + ")$", args.domain) is not None):
            tools = get_active_tools()
            for tool in tools:
                OsintToolBuilder.getTool(tool, {"url": args.domain}).run()
        else:
            print('Domaine non valide : Format : https://domain.tld')