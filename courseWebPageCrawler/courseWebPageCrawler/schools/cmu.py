import os
import re
import datetime

import icalendar
from icalendar import Calendar, Event
from icalendar import vDatetime
from icalendar.parser import Contentline
from icalendar.parser import Contentlines

from ..classes.shared import find_nth
from ..classes.shared import retrieve_element
from ..classes.shared import is_colloquim
from ..classes.shared import is_month
from ..classes.shared import is_formal
from ..classes.shared import is_empty
from ..classes.colloquia import Colloquia

def cmu_executor(my_SSS):

	school = my_SSS.get_school('cmu')
	#Extract an initial content list, the xpath provided has to be manually inspected/found
	my_SSS.extract_content(school.get_name(),'//div[@class="calendar-admin-menu"]')

	my_SSS.extract_ical_content(0, 'https://www.scs.cmu.edu', 0, 'cmu')

	#process the ical file to retrieve the colloquia
	retreive_colloquia(my_SSS)
	
	#Set Official School Name Manually from the school object
	school.set_official_name("Carnegie Mellon University")

def retreive_colloquia(my_SSS):
	cmu = my_SSS.get_school('cmu')
	for elt in my_SSS.get_filtered_content().walk():
		if elt.name == "VEVENT" :

			#the first word of the description is the category of the talk
			Description = elt.get('description')
			category = retrieve_element(Description[0], Description, 0,' ', "", 0, 0)
			#print "CUR: " + category

			#the phrase is passed from the is_colloquim filter in the shared module
			if (is_colloquim(category) == 0):
				continue	#it is not a colloquia
			else:
				#print "CREATING Colloquia with, " + category
				#create new colloquia
				cur = Colloquia()

				cur.set_metadata('description', Description)

				Time = elt.decoded('dtstart')
				cur.set_metadata('date', Time)

				Venue = elt.get('location')
				cur.set_metadata('venue', Venue)

				URL = elt.get('URL')
				cur.set_metadata('url', URL)

				ST_list = get_speaker_topic(Description)
				if len(ST_list) == 1:
					Topic = ST_list[0]
					cur.set_metadata('topic', Topic)
				else:
					Speaker = ST_list[0]
					cur.set_metadata('speaker', Speaker)
					Topic = ST_list[1]
					cur.set_metadata('topic', Topic)

				cmu.push_colloquia(cur)

def get_speaker_topic(Description):
	index = 3
	num_newline = 8
	possible_speaker_topics = []
	while (index < (3*num_newline + 1)):
		index_content = find_nth(Description, "\n", index)
		content = retrieve_element(Description[index_content+1], Description[index_content+1:], 0, "\n", "", 0, 0)
		index += 3
		possible_speaker_topics.append(content)
	count = 0
	#Process the 'Possibles'
	for elt in list(possible_speaker_topics):
		if (is_month(elt) != "NO" or is_empty(elt) == 1 or is_formal(elt) == 1 or len(elt) < 5 or len(elt) > 150):
			possible_speaker_topics.remove(elt)
	
	return possible_speaker_topics