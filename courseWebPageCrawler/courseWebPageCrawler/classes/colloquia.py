import os, sys

import shared

class Colloquia:

	def __init__(self):
		self.topic = 'TBD'
		self.speaker = 'TBD'
		self.date = 'TBD'
		self.venue = 'TBD'
		self.university = 'TBD'
		self.url = 'NONE'
		self.description = 'NONE'
		self.tags = list()

	def set_metadata(self, category, data):

		exec("self." + category + " = data")

		if (category == "speaker") or (category == "topic") or (category == "university"):
			for elt in data.split():
				if(len(elt) < 3): continue
				self.tags.append(elt)
		elif category == "date":
			data = str(data)
			Year = data[:4]
			self.tags.append(Year)
			Month = data[5] + data[6]
			if Month[0] == '0':
				Month = Month[1]
			Month = shared.month_string_converter(Month)
			self.tags.append(Month)

	def print_all(self):
		print "TOPIC: " + self.topic
		print "SPEAKER: " + self.speaker
		print "DATE: " + str(self.date)
		print "VENUE: " + self.venue
		print "UNIV: " + self.university
		print "URL: " + self.url
		print "DESCRIPTION: " + self.description 
		print "TAGS: " + str(self.tags)