import scrapy
import urlparse
from scrapy.http import HtmlResponse

from school import School
import sss

class Extractor():

	def __init__(self):
		pass

	def extract_html(self, school_name, xpath_str):
		return sss.get_school(school_name).get_response().xpath(xpath_str).extract()
		