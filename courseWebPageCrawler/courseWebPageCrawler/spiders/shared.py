import courseWebPageSpider
import urlparse
import re
import datetime
import json
import uiuc
import cornell
import berkeley


cornell_url = "https://www.cs.cornell.edu/events/colloquium"
uiuc_url = "http://cse.illinois.edu/news-events/seminars"
berkeley_url = "http://www.eecs.berkeley.edu/Colloquium/"
uwash_url = "https://www.cs.washington.edu/events/colloquia"
cmu_url = "https://www.scs.cmu.edu/calendar"

#list or allowed domains
edu = "edu"
all_records = []

url_to_school = dict()

def add_url_to_school(key, value):
    url_to_school[key] = value
def get_school_from_url(url):
    return url_to_school[url]

school_data = dict()
def add_school_data(key, value):
    school_data[key] = value
def get_school_data(key, value):
    return school_data[key]
def get_all_school_data():
    return school_data

def extract_html(sss, school_name, xpath_str):
        return sss.get_school(school_name).get_response().xpath(xpath_str).extract()

def date_handler(school_class, content, date_type, dist, Topic, Speaker, Time, Venue, University, URL, Description, Tags):
    for elt in content:

        cur_date_type = 'NO'
        if date_type == "Month":
            cur_date_type = is_month(elt)
        elif date_type == "Day":
            cur_date_type = is_day(elt)

        if (cur_date_type != 'NO'):
            Time = extract_date(cur_date_type, elt, dist, date_type)
            exec (school_class + "." + 'records.append(create_record(Topic, Speaker, Time, Venue, University, URL, Description, Tags))')
            #records.append(shared.create_record(Topic, Speaker, Time, Venue, University, URL, Description, Tags)
def is_empty(s):
    for elt in s:
        if elt != " " or elt.isdigit():
            return 0
    return 1

def is_day(s):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    for day in days:
        if day in s.lower():
            return day[0].upper() + day[1:]
    return 'NO'

def is_month(s):
	months = ['january', 'february', 'march', 'april', 'may', 'june','july', 'august', 'september', 'october', 'november', 'december']
	for month in months:
		if month in s.lower():
			return month[0].upper() + month[1:]
	return 'NO'

def month_converter(month):
    months = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
    return months.index(month) + 1


def day_converter(day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days.index(day) + 1

def extract_date(date_type, elt, dist, typ):

    now = datetime.datetime.now()
    year = now.year
    
    dm = 0
    index = elt.index(date_type) + len(date_type) + dist
    #print elt[index]
    while(elt[index].isnumeric()):
        #print elt[index]
        dm *= 10
        dm += int(elt[index])
        index += 1
  
    if (typ == "Month"):
        date_type = month_converter(date_type)
        return datetime.date(int(year), date_type, dm)
    elif (typ == "Day"):
        date_type = day_converter(date_type)
        #print datetime.date(int(year), dm, date_type)
        return datetime.date(int(year), dm, date_type)

def create_record(Topic, Speaker, Time, Venue, University, URL, Description, Tags):

    record = {'Topic': Topic.encode("utf-8"), 'Speaker': Speaker.encode("utf-8"), 'Time': str(Time), 'Venue': Venue.encode("utf-8"), 'University': University.encode("utf-8"), 'URL': URL.encode("utf-8"), 'Description': Description.encode("utf-8"), 'Tags': Tags.encode("utf-8")}
    return record

def create_date(Day, Month, Year):
	d = datetime.date(Year, Month, Day)
	return d

def retrieve_element(to_find, elt, dist, delimeter, default_to_return, is_URL, reverse):
    if(not reverse):
        index = elt.find(to_find)
    else:
        index = elt.rfind(to_find)
    
    #print elt
    if index != -1:
        if not reverse:
            index += dist
        else:
            index -= dist
        #print elt[index]
    else:
        return default

    to_return_build = ""
    quotes_seen = 0
    if not reverse:
        while(elt[index] != delimeter):

            if (elt[index] == '"'):
                if (is_URL):
                    quotes_seen += 1
                    if quotes_seen == 1:    return to_return_build
                else:
                    return default   

            to_return_build += elt[index]
            index += 1
        if not to_return_build or len(to_return_build) < 2: return default
        return to_return_build
    else:

        while(elt[index] != delimeter):
            elt[index] + " " + to_return_build
            to_return_build = elt[index] + to_return_build
            index -= 1
        if not to_return_build or len(to_return_build) < 2: return default
        return to_return_build

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def add_to_all_records(records):
    for record in records:
        all_records.append(record)


def writeToFile(fileName):
        to_send = dict()
        to_send["records"] = all_records
        working_dir = 'data'     
        #print "LOOK AT JSON HERE!!!: \n"   
        with open(working_dir + '/' + fileName, 'w') as fout:
            json.dump(to_send, fout)

