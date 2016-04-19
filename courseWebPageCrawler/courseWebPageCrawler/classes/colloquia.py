import os, sys

class Colloquia:

	def __init__(self):
		self.topic = 'TBD'
		self.speaker = 'TBD'
		self.date = 'TBD'
		self.venue = 'TBD'
		self.university = 'TBD'
		self.url = 'NONE'
		self.description = 'NONE'
		self.tags = 'NONE'

	def set_metadata(self, category, data):

		exec("self." + category + " = data")

	def print_all(self):
		print "TOPIC: " + self.topic
		print "SPEAKER: " + self.speaker
		print "DATE: " + str(self.date)
		print "VENUE: " + self.venue
		print "UNIV: " + self.university
		print "URL: " + self.url
		print "DESCRIPTION: " + self.description 
		print "TAGS: " + self.tags

	def serialize(self):
		new_str = unicode("$TOPIC: " + self.topic + "\n" + "$SPEAKER: " + self.speaker + "\n" + "$DATE: " + str(self.date) + "\n"  + "$VENUE: " + self.venue + "\n" + "$UNIVERSITY: " + self.university + "\n"  + "$URL: " + self.url + "\n"  + "$DESCRIPTION: " + self.description + "\n"  + "TAGS: " + self.tags + "\n", errors='ignore')
		print "!!!!!!!!!START!!!!!!!!!!"
		print unicode(new_str, errors='ignore')
		print "!!!!!!!!!END!!!!!!!!!!!!"
		return unicode(new_str, errors='ignore')