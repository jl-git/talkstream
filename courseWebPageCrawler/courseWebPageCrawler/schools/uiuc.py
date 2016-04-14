import os
import re
import urlparse
import json
import datetime

from ..classes.sss import SSS
from ..classes.shared import months

"""
#Records
records = [dict()]

def speaker_topic_url_handler(possible_colloquims):
	#print possible_colloquims
	count = 1
	for elt in possible_colloquims:
		month = shared.is_month(elt)
		if (month == 'NO'):
			continue

		URL = shared.retrieve_element('ref=', elt, 5, '<', "", 1, 0)
		Speaker = shared.retrieve_element('<br>', elt, 4, '<', "", 0, 0)
		Topic = shared.retrieve_element('<em>', elt, 4, '<','TBD', 0, 0)

		records[count]['URL'] = URL.encode("utf-8")
		records[count]['Speaker'] = Speaker.encode("utf-8")
		records[count]['Topic'] = Topic.encode("utf-8")
		count += 1
"""

def uiuc_executor(my_SSS):
	#get school object stored for respective school from SSS(Super Seminar Scraper)
	school = my_SSS.get_school('uiuc')
	#Extract an initial content list, the xpath provided has to be manually inspected/found
	my_SSS.extract_content(school.get_name(),'//div[@class="content"]/p')
	#gets a list equal to the size of elements we actually want, filters based on months
	#if any of the elements of months exists it is not filtered out
	my_SSS.filter_content(school.get_name(), months)

	my_SSS.retrieve_dates(school.get_name(), "Month", 1)
	
	my_SSS.set_content_list(my_SSS.get_filtered_content())
	#Topic
	my_SSS.retrieve_metadata(school.get_name(), 'topic', '<em>', 4, '<','TBD', 0, 0)
	#Speaker
	my_SSS.retrieve_metadata(school.get_name(), 'speaker', '<br>', 4, '<', "", 0, 0)
	#URL
	my_SSS.retrieve_metadata(school.get_name(), 'url', 'ref=', 5, '<', "", 1, 0)
	#Date
	
	#Set Venue and Official School Name Manually from the school object
	school.set_venue("NCSA Room 1030")
	school.set_official_name("University of Illinois at Urbana Champaign")
