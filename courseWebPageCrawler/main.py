import os
from datetime import datetime

from courseWebPageCrawler.classes.sss import SSS
from courseWebPageCrawler.classes.school import School
#from courseWebPageCrawler.classes.colloquia import Colloquia

from courseWebPageCrawler.schools.uiuc import uiuc_executor
#from courseWebPageCrawler.schools.cornell import cornell_executor
#from courseWebPageCrawler.schools.berkeley import berkeley_executor
#from courseWebPageCrawler.schools.uwash import uwash_executor
#from courseWebPageCrawler.schools.cmu import cmu_executor

#sys.path.append( /Users/batuinal1/Desktop/Git/talkstream/courseWebPageCrawler/courseWebPageCrawler/classes )

#Define url of school here
cornell_url = "https://www.cs.cornell.edu/events/colloquium"
uiuc_url = "http://cse.illinois.edu/news-events/seminars"
berkeley_url = "http://www.eecs.berkeley.edu/Colloquium/"
uwash_url = "https://www.cs.washington.edu/events/colloquia"
cmu_url = "https://www.scs.cmu.edu/calendar"
#add new <school_url> here

def main():

	#print current date and time
	print str(datetime.now())

	#create a new SSS(Super Seminar Scraper) Object called my_SSS
	my_SSS = SSS()
	
	#create a new School Object for UIUC
	uiuc = School("uiuc", uiuc_url)
	#feed our school to our super seminar scraper
	my_SSS.add_school(uiuc)

	#Berkeley
	#berkeley = School("berkeley", berkeley_url)
	#my_SSS.add_school(berkeley)

	#Cornell
	#cornell = School("cornell", cornell_url)
	#my_SSS.add_school(cornell)

	#UWash
	#uwash = School("uwash", uwash_url)
	#my_SSS.add_school(uwash)

	#CMU
	#cmu = School("cmu", cmu_url)
	#my_SSS.add_school(cmu)

	#add new school here ...

	#print my_SSS.get_school_data()

	#Use Scrapy to get raw_html of website
	my_SSS.scrape_data()

	#TODO
	uiuc_executor(my_SSS)

	count = 0
	for item in my_SSS.get_school('uiuc').get_colloquim():
		print str(count) + ": "
		print item.print_all()
		count += 1

if __name__ == "__main__":
	main()



