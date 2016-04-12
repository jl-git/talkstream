import os
from datetime import datetime

from sss import SSS
from school import School
#from classes.dir import Dir

import courseWebPageCrawler.spiders.shared

cornell_url = "https://www.cs.cornell.edu/events/colloquium"
uiuc_url = "http://cse.illinois.edu/news-events/seminars"
berkeley_url = "http://www.eecs.berkeley.edu/Colloquium/"
uwash_url = "https://www.cs.washington.edu/events/colloquia"
cmu_url = "https://www.scs.cmu.edu/calendar"
#add new <school_url> here

def execute(SSS, school_name):
	#get school object stored for respective school from SSS(Super Seminar Scraper)
	school = SSS.get_school(school_name)
	#Extract an initial content list, the xpath provided has to be manually inspected/found
	SSS.extract_content(school.get_name(),'//div[@class="content"]/p')
	#gets a list equal to the size
	SSS.filter_content(courseWebPageCrawler.spiders.shared.months)
	print school.get_name()
	school.set_name("HELLO")
	print SSS.get_school(school_name).get_name()
	#my_SSS.retrieve_element(content_list, my_SSS ) #TODO
	#print content
	#shared.date_handler('uiuc',content,"Month", 1, "", "", "", "NCSA Room 1040", "UIUC", "", "", "")
	#uiuc.speaker_topic_url_handler(content)
	#shared.add_to_all_records(uiuc.records[1:])

def main():

	#print current date and time
	print str(datetime.now())

	#create a new SSS(Super Seminar Scraper) Object
	my_SSS = SSS()
	
	#create a new School Object for UIUC
	uiuc = School("uiuc", uiuc_url)
	#feed our school to our super seminar scraper
	my_SSS.add_school(uiuc)

	#Berkeley
	berkeley = School("berkeley", berkeley_url)
	my_SSS.add_school(berkeley)

	#Cornell
	cornell = School("cornell", cornell_url)
	my_SSS.add_school(cornell)

	#UWash
	uwash = School("uwash", uwash_url)
	my_SSS.add_school(uwash)

	#CMU
	cmu = School("cmu", cmu_url)
	my_SSS.add_school(cmu)

	#print my_SSS.get_school_data()

	#Use Scrapy to get raw_html of website
	my_SSS.scrape_data()

	execute(my_SSS, "uiuc")

if __name__ == "__main__":
	main()



