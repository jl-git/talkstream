import os
import courseWebPageSpider
import shared
import re
import urlparse
import json
import datetime

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
	counter = 0
	for rec in records:
		if counter != 0: 
			print str(counter) + ": " 
			print rec
		counter += 1
"""
#1st <br> --> Name
#1st href --> URL   	Edge_Case: NO HREF
#1st <em> --> Topic 	Edge_Case: NO <em>, yes <em> but very small <em> for e.g: 2