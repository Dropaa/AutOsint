from abc import ABC, abstractmethod


class OsintTool(ABC):
	@abstractmethod
	def run(self):
		pass
	
	@abstractmethod
	def output(self):
		pass

 