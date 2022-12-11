from OsintTool import OsintTool
from Shodan import Shodan
from UrlScan import UrlScan


class OsintToolBuilder:
	@staticmethod
	def getTool(tool, params) -> OsintTool:
		match tool:
			case "urlscan":
				return UrlScan(params)	
			case "shodan":
				return Shodan(params)
			case _:
				return UrlScan(params)