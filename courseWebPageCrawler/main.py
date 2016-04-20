import os
from datetime import datetime

from courseWebPageCrawler.classes.sss import SSS
from courseWebPageCrawler.classes.school import School
#from courseWebPageCrawler.classes.colloquia import Colloquia

from courseWebPageCrawler.schools.uiuc import uiuc_executor
from courseWebPageCrawler.schools.cornell import cornell_executor
from courseWebPageCrawler.schools.berkeley import berkeley_executor
from courseWebPageCrawler.schools.uwash import uwash_executor
from courseWebPageCrawler.schools.cmu import cmu_executor
#import new cusom executor of form from courseWebPageCrawler.schools.<school_name> import <school_name>_executor..

#Define url of school here
cornell_url = "https://www.cs.cornell.edu/events/colloquium"
uiuc_url = "http://cse.illinois.edu/news-events/seminars"
berkeley_url = "http://www.eecs.berkeley.edu/Colloquium/"
uwash_url = "https://www.cs.washington.edu/events/colloquia"
cmu_url = "https://www.scs.cmu.edu/calendar"
#add new <school_url> here..

def main():
	
	print str(datetime.now())	#print current date and time

	my_SSS = SSS('my_SSS')	#create a new SSS(Super Seminar Scraper) Object called my_SSS
	
	uiuc = School("uiuc", uiuc_url)	#create a new School Object for UIUC
	my_SSS.add_school(uiuc)	#feed our school to our super seminar scraper

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

	#add new school here..

	my_SSS.scrape_data()	#Use Scrapy to get raw_html of website

	#call executors once schools have been added and SSS object's scrape_data() method has been called
	uiuc_executor(my_SSS)
	berkeley_executor(my_SSS)
	cornell_executor(my_SSS)
	uwash_executor(my_SSS)
	cmu_executor(my_SSS)
	#add new <school_name>.py file to schools folder and write a custom executor..

	#normalize and save all the data into a file (append to existing records)
	#also write to alltalks.json for Front-end to process
	my_SSS.save()

if __name__ == "__main__":
	main()