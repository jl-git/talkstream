import scrapy
from scrapy.http import HtmlResponse
from courseWebPageCrawler.items import CourseWebPage

class School:

	def __init__(self, name, url):
		"""
            name: name of school for e.g: "cmu"
            url: url of the school's colloquia site
        """
		#metadata, raw_content, url
		self.name = name
		self.url = url
		self.parser_type = "html"	#parser_type: "html" or "ical", string
 		self.colloquia = list()
 		self.response = "NULL_RESPONSE"

	def get_name(self):
		return self.name

	def get_url(self):
		return self.url

	def set_url(self, url):
		self.url = url

	def set_parser_type(self, parser_type):
		self.parser_type = parser_type

	def push_colloquia(self, colloquia):
		self.append(colloquia)

	def get_colloquia(self, index):
		if (index < 0 or index >= len(self.colloquia)):
			return -1
		return self.colloquia[index]

	def set_response(self, response):
		self.response = response

	def get_response(self):
		return self.response