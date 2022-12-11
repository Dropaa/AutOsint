from OsintTool import OsintTool
from Shodan import Shodan
from TheHarvester import TheHarvester
from UrlScan import UrlScan
from Dnscan import Dnscan


class OsintToolBuilder:
	@staticmethod
	def getTool(tool, params) -> OsintTool:
		match tool:
			case "urlscan":
				return UrlScan(params)	
			case "shodan":
				return Shodan(params)
			case "theharvester":
				return TheHarvester(params)
			case "dnscan":
				return Dnscan(params)
			case _:
				return UrlScan(params)