import os
import courseWebPageSpider
import re
import urlparse
import json
import datetime
import shared

#Records
records = [dict()]

def is_colloquim(category):
	negative_category = ["Career", "Fun", "Special", "Distinguished", "Conference/Workshop"]
	if category in negative_category:
		return 0
	return 1

def is_formal(elt):
	negative_category = ["Ph.D", "College", "University", "Engineer", "Engineering", "Institute", "Graduate", "Student", "Hall", "Campus", "Carnegie", "Professor", "Scientist", "Centers", "Auditorium", "Room", "Postdoctoral", "Fellow", "Abstract:", '[View', 'Microsoft', 'Researcher', 'Department', 'Instructor', 'Visiting', 'Partner']
	for negative in negative_category:
		if negative in elt:
			return 1
	return 0

def get_speaker_topic(Description):
	index = 3
	num_newline = 8
	possible_speaker_topics = []
	while (index < (3*num_newline + 1)):
		index_content = shared.find_nth(Description, "\n", index)
		content = shared.retrieve_element(Description[index_content+1], Description[index_content+1:], 0, "\n", "", 0, 0)
		index += 3
		possible_speaker_topics.append(content)
	count = 0
	#Process the 'Possibles'
	for elt in list(possible_speaker_topics):
		if (shared.is_month(elt) != "NO" or shared.is_empty(elt) == 1 or is_formal(elt) == 1 or len(elt) < 5 or len(elt) > 150):
			#print "Removing: " + elt
			possible_speaker_topics.remove(elt)

	#print len(possible_speaker_topics)
	for elt in possible_speaker_topics:
		#print str(count) + ": " + elt
		count += 1
	
	return possible_speaker_topics	
	#print "Speaker: " + Speaker
	#print "Topic: " + Topic
				#print Description[:index_Topic]

def create_records(content):
	count = 1
	for elt in content.walk():
		#print component.get('description') != 'Seminars'
		#Seminars
		#SEMINAR/COLOQ distinction
		#Get Speaker
		if elt.name == "VEVENT" :
			Description = elt.get('description')
			#the first word of the description is the category of the talk
			category = shared.retrieve_element(Description[0], Description, 0,' ', "", 0, 0)
			if (is_colloquim(category) == 0):
				continue
			else:
				#print str(count) + ': '
				Topic = "TBD" 
				Speaker = "TBD"
				Time = elt.decoded('dtstart')
				Venue = elt.get('location')
				University = 'Carnegie Mellon University'
				URL = elt.get('URL')
				#Description = elt.get('summary')
				Tags = ""
				count += 1
				ST_list = get_speaker_topic(Description)
				if len(ST_list) == 1:
					Topic = ST_list[0]
				else:
					Speaker = ST_list[0]
					Topic = ST_list[1]

				records.append(shared.create_record(Topic, Speaker, Time, Venue, University, URL, Description, Tags))
