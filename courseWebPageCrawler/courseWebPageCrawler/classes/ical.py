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


def ical_get_calendar_url(content, index, beg):
	URL = shared.retrieve_element('ref=', content[index], 5, '<', "", 1, 0)
	if (beg == ""): return URL
	return beg + URL

def ical_get_content(URL, is_broken, school_name):
	response = urllib2.urlopen(str(URL)).read()
	
	if (is_broken):
		#classname.fix_ics
		response = uwash.fix_ics(response)
	content = Calendar.from_ical(response)
	return content

def ical_get_content_from_url(content, index, beg, is_broken, school_name):
	return get_content(get_calendar_url(content, index, beg), is_broken, school_name)