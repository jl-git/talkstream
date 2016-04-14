import os
import courseWebPageSpider
import re
import urlparse
import json
import datetime
import shared
import ical

import icalendar
from icalendar import Calendar, Event
from icalendar import vDatetime
from icalendar.parser import Contentline
from icalendar.parser import Contentlines

#Records
records = [dict()]


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

def fix_ics(response):
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