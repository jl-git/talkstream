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

from ..classes.shared import find_nth
from ..classes.shared import retrieve_element
from ..classes.colloquia import Colloquia

def uwash_executor(my_SSS):

	school = my_SSS.get_school('uwash')
	#Extract an initial content list, the xpath provided has to be manually inspected/found
	my_SSS.extract_content(school.get_name(),'//div[@id="feeds"]/a')

	my_SSS.extract_ical_content(1, "", 1, 'uwash')

	retreive_colloquia(my_SSS)
	
	#Set Venue and Official School Name Manually from the school object
	school.set_official_name("University of Washington")

def retreive_colloquia(my_SSS):
	uwash = my_SSS.get_school('uwash')

	for elt in my_SSS.get_filtered_content().walk():
		if elt.name == "VEVENT":
			cur = Colloquia()

			index_S = find_nth(elt.get('summary'), ":", 1)
			Speaker = retrieve_element(elt.get('summary')[index_S], elt.get('summary')[index_S:], 2,':', "NO", 0, 0)
			cur.set_metadata('speaker', Speaker)

			index_T = find_nth(elt.get('summary'), ":", 2)
			Topic = elt.get('summary')[index_T+2:]
			cur.set_metadata('topic', Topic)
			
			Description = elt.get('description')
			cur.set_metadata('description', Description)

			Time = elt.decoded('dtstart')
			cur.set_metadata('date', Time)

			Venue = elt.get('location')
			cur.set_metadata('venue', Venue)

			URL = elt.get('URL')
			cur.set_metadata('url', URL)

			uwash.push_colloquia(cur)
