import os
import re
import urlparse
import json
import datetime

import icalendar
from icalendar import Calendar, Event
from icalendar import vDatetime
from icalendar.parser import Contentline
from icalendar.parser import Contentlines

#Records
records = [dict()]

def uwash_executor(my_SSS):

	school = my_SSS.get_school('uwash')
	#Extract an initial content list, the xpath provided has to be manually inspected/found
	my_SSS.extract_content(school.get_name(),'//div[@id="feeds"]/a')

	my_SSS.extract_ical_content(1, "", 1, 'uwash')

	count = 0
	for elt in my_SSS.get_filtered_content():
		print str(count) + elt
		count += 1

	#my_SSS.retrieve_dates(school.get_name(), "Month", 1)
	
	#my_SSS.set_content_list(my_SSS.get_filtered_content())
	#Topic
	#my_SSS.retrieve_metadata(school.get_name(), 'topic', '<em>', 4, '<','TBD', 0, 0)
	#Speaker
	#my_SSS.retrieve_metadata(school.get_name(), 'speaker', '<br>', 4, '<', "", 0, 0)
	#URL
	#my_SSS.retrieve_metadata(school.get_name(), 'url', 'ref=', 5, '<', "", 1, 0)
	#Date
	
	#Set Venue and Official School Name Manually from the school object
	school.set_venue("NCSA Room 1030")
	school.set_official_name("University of Illinois at Urbana Champaign")
	"""
	possible_links = response.xpath('//div[@id="feeds"]/a').extract()
            link = ical.get_calendar_url(possible_links, 1, '')
            content = ical.get_content(link, 1, 'uwash')
            uwash.create_records(content)
            shared.add_to_all_records(uwash.records[1:])
            #shared.send('uwash.json', uwash.records[1:])
    """


def create_records(content):
	count = 1
	for elt in content.walk():
		if elt.name == "VEVENT":

			index_S = shared.find_nth(elt.get('summary'), ":", 1)
			Speaker = shared.retrieve_element(elt.get('summary')[index_S], elt.get('summary')[index_S:], 2,':', "NO", 0, 0)
			
			index_T = shared.find_nth(elt.get('summary'), ":", 2)
			Topic = elt.get('summary')[index_T+2:]
			
			Description = elt.get('description')
			Time = elt.decoded('dtstart')
			Venue = elt.get('location')
			University = 'University of Washington'
			URL = elt.get('URL')
			Tags = ""
			records.append(shared.create_record(Topic, Speaker, Time, Venue, University, URL, Description, Tags))
			#print str(count) + ": "
			#print records[-1]
			count += 1

def uwash_fix_ics(response):
	removed_file = 0
	for line in Contentlines.from_ical(response):
		if ((not removed_file) and os.path.exists("uwash.ics")):
			os.remove('uwash.ics')
			removed_file = 1
			
		if line.find("X-WR-$CALNAME") != -1:
			with open("uwash.ics","a+") as f:
				f.write('X-WR-CALNAME:UW CSE Colloquium Calendar\n')
				continue
		with open("uwash.ics","a+") as f:
			#print "HERE"
			f.write(line.encode("utf-8"))
			f.write('\n')
	content = open('uwash.ics').read()
	return content