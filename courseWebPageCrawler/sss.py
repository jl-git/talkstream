import scrapy
from courseWebPageCrawler.spiders.courseWebPageSpider import CourseWebPageSpider
from scrapy.spiders import CrawlSpider
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from courseWebPageCrawler.spiders.shared import add_url_to_school
from courseWebPageCrawler.spiders.shared import add_school_data
from courseWebPageCrawler.spiders.shared import get_all_school_data
from courseWebPageCrawler.spiders.shared import extract_html
from extractor import Extractor

class SSS:


    def __init__(self):

        #metadata, raw_content, url
        self.school_data = dict()
        self.spider = CourseWebPageSpider(CrawlSpider)
        
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

    def scrape_data(self):
        """
            Scrapes the raw html of all schools in school_data dict
        """
        #setup enviorment for Scrapy and shared file
        for school in self.school_data.itervalues():
            self.spider.start_urls.append(school.get_url())
            add_url_to_school(school.get_url(), school.get_name())
            add_school_data(school.get_name(), school)

        #run multi-threaded crawlers
        runner = CrawlerRunner()
        d = runner.crawl(self.spider)
        d.addBoth(lambda _: reactor.stop())
        reactor.run() #

        #copy back school_data from shared
        for school in get_all_school_data().itervalues():
            self.school_data[school.get_name()] = school

        #for items in self.school_data.itervalues():
            #print items.get_response()
        #print self.school_data

    def extract_content(self, school_name, xpath_str):
        return extract_html(self, school_name, xpath_str)
