import os, sys

class Colloquia:

	def __init__(self):
		self.topic = str()
		self.speaker = str()
		self.date = str()
		self.venue = str()
		self.university = str()
		self.url = str()
		self.description = str()
		self.tags = ""

	def set_metadata(self, category, data):
		exec("self." + category + " = data")

	def print_all(self):
		print "TOPIC: " + self.topic
		print "SPEAKER: " + self.speaker
		print "DATE: " + self.date
		print "VENUE: " + self.venue
		print "UNIV: " + self.university
		print "URL: " + self.url
		print "DESCRIPTION: " + self.description 
		print "TAGS: " + self.tags