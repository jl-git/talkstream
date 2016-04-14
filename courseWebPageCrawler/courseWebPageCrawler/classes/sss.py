import os, sys

import scrapy
from scrapy.spiders import CrawlSpider
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from ..spiders.courseWebPageSpider import CourseWebPageSpider

import shared
from colloquia import Colloquia

class SSS:

    def __init__(self):

        #metadata, raw_content, url
        self.school_data = dict()
        self.spider = CourseWebPageSpider(CrawlSpider)
        self.content_list = list() #dummy variable held for parsing
        self.filtered_content = list() #dummy variable held during parsing
        
    def add_school(self, School):
        """
            School: school object 
            Adds school to school_data dict
        """
        self.school_data[School.get_name()] = School

    def get_school_data(self):
        return self.school_data

    def get_school(self, name):
        data = self.school_data.get(name)
        if data:
            return data
        return -1
    def get_content_list(self):
        return self.content_list

    def set_content_list(self, content_list):
        self.content_list = content_list

    def get_filtered_content(self):
        return self.filtered_content

    def scrape_data(self):
        """
            Scrapes the raw html of all schools in school_data dict
        """
        #setup enviorment for Scrapy and shared file
        for school in self.school_data.itervalues():
            self.spider.start_urls.append(school.get_url())
            shared.add_url_to_school(school.get_url(), school.get_name())
            shared.add_school_data(school.get_name(), school)

        #run multi-threaded crawlers
        runner = CrawlerRunner()
        d = runner.crawl(self.spider)
        d.addBoth(lambda _: reactor.stop())
        reactor.run() #

        #copy back school_data from shared
        for school in shared.get_all_school_data().itervalues():
            self.school_data[school.get_name()] = school

    def extract_content(self, school_name, xpath_str):
        self.content_list = shared.extract_html(self, school_name, xpath_str)

    def filter_content(self, school_name, list_to_find):
        self.filtered_content = shared.filter_list(self.content_list, list_to_find)
        for elt in self.get_filtered_content():
            self.get_school(school_name).push_colloquia(Colloquia())

    def retrieve_metadata(self, school_name, category, to_find, dist, delimeter, default_to_return, is_URL, reverse):
        count = 0
        for elt in self.get_content_list():
            metadata = shared.retrieve_element(to_find, elt, dist, delimeter, default_to_return, is_URL, reverse)
            self.get_school(school_name).get_colloquim()[count].set_metadata(category, metadata)
            count += 1
    def retrieve_dates(self, school_name, date_type, dist):
        count = 0
        for elt in self.get_filtered_content():
            metadata = shared.extract_date(elt, dist, date_type)
            self.get_school(school_name).get_colloquim()[count].set_metadata('date', str(metadata))
            count += 1

