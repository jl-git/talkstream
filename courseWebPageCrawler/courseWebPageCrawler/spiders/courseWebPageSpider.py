import os
import re
import urlparse
import json

import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

from courseWebPageCrawler.items import CourseWebPage

from ..classes.shared import url_to_school
from ..classes.shared import set_school_response
from ..classes.shared import edu

class CourseWebPageSpider(CrawlSpider):

    name = 'courseWebPageCrawler'
    
    school_name = ""
    start_urls = list()
    school_data = dict()
    url_to_school = dict()
    #start_urls = [shared.cornell_url, shared.uiuc_url, shared.berkeley_url, shared.uwash_url, shared.cmu_url]
    allowed_domains = [edu]
    
    def parse(self, response):

        self.log('A response from %s just arrived!' % response.url)

        copy = response.copy()
        school_name = url_to_school[response.url]
        print school_name
        set_school_response(school_name, response)