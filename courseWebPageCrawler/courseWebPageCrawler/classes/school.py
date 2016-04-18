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
 		self.colloquim = list()
 		self.response = "NULL_RESPONSE"

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_url(self):
		return self.url

	def set_url(self, url):
		self.url = url

	def set_parser_type(self, parser_type):
		self.parser_type = parser_type

	def push_colloquia(self, colloquia):
		self.colloquim.append(colloquia)

	def get_colloquia(self, index):
		if (index < 0 or index >= len(self.colloquim)):
			return -1
		return self.colloquim[index]

	def get_colloquim(self):
		return self.colloquim

	def clear_colloquim(self):
		self.colloquim = list()

	def set_response(self, response):
		self.response = response

	def get_response(self):
		return self.response

	def set_venue(self, venue_name):
		for elt in self.colloquim:
			elt.set_metadata('venue', venue_name)

	def set_official_name(self, official_name):
		for elt in self.colloquim:
			elt.set_metadata('university', official_name)