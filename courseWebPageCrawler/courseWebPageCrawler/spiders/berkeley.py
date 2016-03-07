import os
import courseWebPageSpider
import re
import urlparse
import json
import datetime
import shared

#Records
records = [dict()]

def speaker_topic_url_handler(possible_colloquims):
	count = 0
	for elt in possible_colloquims:

		if (count%2):
			#retrieve_element(to_find, elt, dist, default, is_URL)
			URL = shared.retrieve_element('ref=', elt, 5, '<', "", 1, 0)
			Topic = shared.retrieve_element('html">', elt, 6, '<', 'TBD', 0, 0)
			Speaker = shared.retrieve_element('</a></strong>', elt, 1, '>', 'TBD', 0, 1)
			
			records[count/2 + 1]['URL'] = URL
			records[count/2 + 1]['Speaker'] = Speaker
			records[count/2 + 1]['Topic'] = Topic
		count += 1
"""
	counter = 0
	for rec in records:
		if counter != 0: 
			print str(counter) + ": " 
			print rec
		counter += 1
"""