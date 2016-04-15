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

        """
        if (response.url == shared.cornell_url):
            print "GOTCHAAAA --> CORNELL\n"
            #Extracts Dates of the Colloqiums 
            content = response.xpath("//h2").extract()
            #Builds the correct_size-Vector with so_far known info and date_handler
            shared.date_handler('cornell', content, "Day", 1, "", "", "", "G01 Gates Hall - Mentor's Lecture Hall", "Cornell University", "", "", "")
            #Extracts the speaker name, the topic and the url of the speaker
            cornell.speaker_topic_url_handler(response.xpath("//h4").extract())
            #Cleans the vector of dummy elements
            cornell.clean_no_colloqiums()
            #Send Processed Records to be Written to .json file
            shared.add_to_all_records(cornell.records)
            #shared.send('cornell.json', cornell.records)

        elif (response.url == shared.uiuc_url):
            print "GOTCHAAAA --> UIUC\n"

            content = response.xpath('//div[@class="content"]/p').extract()
            shared.date_handler('uiuc',content,"Month", 1, "", "", "", "NCSA Room 1040", "UIUC", "", "", "")
            uiuc.speaker_topic_url_handler(content)
            shared.add_to_all_records(uiuc.records[1:])

        elif (response.url == shared.berkeley_url):
            print "GOTCHAAAA --> Berkeley\n"
            
            #Extract pair of <Date, Speaker_topic_URL> as a list where, even numbered index(n) is a date, 
            #n+1 numbered index is its respective Speaker,Topic,URL
            content = response.xpath('//table[2]/tr/td').extract()
            shared.date_handler('berkeley',content,"Month", 1, "", "", "", "HP Auditorium, 306 Soda Hall", "University of California, Berkeley", "", "", "")
            berkeley.speaker_topic_url_handler(content)
            shared.add_to_all_records(berkeley.records[1:])

        elif (response.url == shared.uwash_url):
            print "GOTCHAAAA --> UWash\n"
            #<div id="feeds">
            possible_links = response.xpath('//div[@id="feeds"]/a').extract()
            link = ical.get_calendar_url(possible_links, 1, '')
            content = ical.get_content(link, 1, 'uwash')
            uwash.create_records(content)
            shared.add_to_all_records(uwash.records[1:])
            #shared.send('uwash.json', uwash.records[1:])

        elif (response.url == shared.cmu_url):
            print "GOTCHAAAA --> CMU\n"
            possible_links = response.xpath('//div[@class="calendar-admin-menu"]').extract()
            link = ical.get_calendar_url(possible_links, 0, 'https://www.scs.cmu.edu')
            content = ical.get_content(link, 0, 'cmu')
            cmu.create_records(content)
            shared.add_to_all_records(cmu.records[1:])
            #shared.send('cmu.json', cmu.records[1:])

        shared.writeToFile("alltalks.json")
        """

"""
"records": [
  {
    "Topic" : "Program Analysis and Transformation for Scientific Computing",
    "Speaker" : "Paul Hovland",
    "Time" : "2015-10-07 09:30",
    "Venue" : "Gould-Simpson 701",
    "University" : "University of Arizona",
    "URL" : "https://www.cs.arizona.edu/news/events/evdetail.html?ID=681",
    "Description" : "We discuss several applications of program analysis and transformation in scientific computing. We begin with a discussion of automatic empirical performance tuning (autotuning) techniques and strategies for dealing with multiple, competing objectives (such as time and power). We continue with a discussion of automatic (also called algorithmic) differentiation techniques for computing the derivatives of functions defined by computer subprograms. We conclude with a consideration of program verification, with an emphasis on proving the equivalence of two implementations.",
    "Tags" : ["Scientific Computing", "University of Arizona"]
  },
"""
