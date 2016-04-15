import os
import re
import urlparse
import json
import datetime

from ..classes.sss import SSS
from ..classes.shared import months

def berkeley_filter(content_list):
	new_list = list()
	count = 0
	for elt in content_list:
		if (count%2):
			new_list.append(elt)
		count += 1
	return new_list

def berkeley_executor(my_SSS):
	#get school object stored for respective school from SSS(Super Seminar Scraper)
	school = my_SSS.get_school('berkeley')
	my_SSS.extract_content(school.get_name(), '//table[2]/tr/td')

	my_SSS.filter_content(school.get_name(), months)

	#Date
	my_SSS.retrieve_dates(school.get_name(), "Month", 1)
	
	#since the format of our current list of elements is where even indexed ones are entries we want, odd are ones we do not want
	#so we simply filter the odd indexed ones out (this is a special case scenario due to berkeley's structure)
	my_SSS.set_content_list(berkeley_filter(my_SSS.get_content_list()))

	#Topic
	my_SSS.retrieve_metadata(school.get_name(), 'topic', 'html">', 6, '<', 'TBD', 0, 0)
	#Speaker
	my_SSS.retrieve_metadata(school.get_name(), 'speaker', '</a></strong>', 1, '>', 'TBD', 0, 1)
	#URL
	my_SSS.retrieve_metadata(school.get_name(), 'url', 'ref=', 5, '<', "", 1, 0)
	
	#Set Venue and Official School Name Manually from the school object
	school.set_venue("HP Auditorium, 306 Soda Hall")
	school.set_official_name("University of California, Berkeley")