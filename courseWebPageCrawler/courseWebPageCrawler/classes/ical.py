import os
import urllib2
import icalendar
from icalendar import Calendar, Event
from icalendar import vDatetime
from icalendar.parser import Contentline
from icalendar.parser import Contentlines
from datetime import datetime
import vobject

import shared
import uwash


def get_calendar_url(content, index, beg):
	URL = shared.retrieve_element('ref=', content[index], 5, '<', "", 1, 0)
	if (beg == ""): return URL
	return beg + URL

def get_content(URL, broken, class_name):
	response = urllib2.urlopen(str(URL)).read()
	
	if (broken):
		#classname.fix_ics
		response = uwash.fix_ics(response)
	content = Calendar.from_ical(response)
	return content

"""
response = urllib2.urlopen('https://www.scs.cmu.edu/calendar/export.ics')

gcal = Calendar.from_ical(response.read())
count = 0
for component in gcal.walk():
	print component.get('description')
	#SEMINAR/COLOQ distinction
	#Get Speaker
	if component.name == "VEVENT":
		#get start date
		print component.decoded('dtstart')
		#print vDatetime.from_ical(x)
		print component.get('summary')
		print component.get('location')
		print component.get('url')
        count += 1
		
print count
#print html
# http://stackoverflow.com/questions/3408097/parsing-files-ics-icalendar-using-python
"""