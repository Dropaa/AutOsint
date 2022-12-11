import json
import sys

from OsintToolBuilder import OsintToolBuilder


def get_active_tools():
    file = open("conf.json", "r")
    data = json.load(file)
    file.close()
    return [tool for tool in data["activeTools"] if data["activeTools"][tool] == True]

if __name__ == "__main__":
    # read config file and loop where "use = yes"
    tools = get_active_tools()
    url = sys.argv[1]
    for tool in tools:
        OsintToolBuilder.getTool(tool, {"url": url}).run()
    