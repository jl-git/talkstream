import os, sys

class Colloquia:

	def __init__(self):
		self.topic = 'TBD'
		self.speaker = 'TBD'
		self.date = 'TBD'
		self.venue = 'TBD'
		self.university = str()
		self.url = str()
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