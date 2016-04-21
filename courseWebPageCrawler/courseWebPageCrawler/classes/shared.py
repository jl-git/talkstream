import os, sys
import urlparse
import re
import datetime
import json
import csv

import urllib2
import icalendar
from icalendar import Calendar, Event
from icalendar import vDatetime
from icalendar.parser import Contentline
from icalendar.parser import Contentlines

import vobject

#from ..schools.uwash import uwash_fix_ics

cornell_url = "https://www.cs.cornell.edu/events/colloquium"
uiuc_url = "http://cse.illinois.edu/news-events/seminars"
berkeley_url = "http://www.eecs.berkeley.edu/Colloquium/"
uwash_url = "https://www.cs.washington.edu/events/colloquia"
cmu_url = "https://www.scs.cmu.edu/calendar"

months = ['january', 'february', 'march', 'april', 'may', 'june','july', 'august', 'september', 'october', 'november', 'december']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

#list or allowed domains
edu = "edu"

global speaker_date
speaker_date = list()
global all_records
all_records = []
global date_count
date_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
def set_school_response(school_name, response):
    school_data[school_name].set_response(response)

def extract_html(sss, school_name, xpath_str):
        return sss.get_school(school_name).get_response().xpath(xpath_str).extract()

def filter_list(content, list_to_find):
    """
        Filters the list of contents by searching wether any one of the elements in the list_to_find exists
        If it does not, removes the element from contents
        returns a new list of contents

        content: list of strings, the content to filter
        list_to_find: list of strings, the filter list
    """
    new_content = list()
    for item in content:
        for elt in list_to_find:
            if (item.lower().find(elt) != -1):
                new_content.append(item)
    return new_content

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

def month_string_converter(elt):
    months = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
    return months[int(elt)]

def day_converter(day):
    return days.index(day) + 1

def extract_date(elt, dist, date_type):
    #print "ELT IS: " + elt 
    cur_date_type = 'NO'
    if date_type == "Month": 
        cur_date_type = is_month(elt)
    elif date_type == "Day":
        cur_date_type = is_day(elt)

    now = datetime.datetime.now()
    year = now.year
    
    dm = 0
    index = elt.index(cur_date_type) + len(cur_date_type) + dist
    #print elt[index]
    while(elt[index].isnumeric()):
        #print elt[index]
        dm *= 10
        dm += int(elt[index])
        index += 1
    #print "DM: " + str(dm)

    if date_type == "Day":
        day = 0
        index += 1
        while(elt[index].isnumeric()):
            #print elt[index]
            day *= 10
            day += int(elt[index])
            index += 1
    #print cur_date_type
    if (date_type == "Month"):
        cur_date_type = month_converter(cur_date_type)
        return datetime.date(int(year), cur_date_type, dm)
    elif (date_type == "Day"):
        return str(datetime.date(int(year), dm, day))

def create_record(Topic, Speaker, Time, Venue, University, URL, Description, Tags):

    record = {'Topic': Topic.encode("utf-8"), 'Speaker': Speaker.encode("utf-8"), 'Time': str(Time), 'Venue': Venue.encode("utf-8"), 'University': University.encode("utf-8"), 'URL': URL.encode("utf-8"), 'Description': Description.encode("utf-8"), 'Tags': Tags}
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
        return default_to_return

    to_return_build = ""
    quotes_seen = 0
    if not reverse:
        while(elt[index] != delimeter):

            if (elt[index] == '"'):
                if (is_URL):
                    quotes_seen += 1
                    if quotes_seen == 1:    return to_return_build
                else:
                    return default_to_return   

            to_return_build += elt[index]
            index += 1
        if not to_return_build or len(to_return_build) < 2: return default_to_return
        return to_return_build
    else:

        while(elt[index] != delimeter):
            elt[index] + " " + to_return_build
            to_return_build = elt[index] + to_return_build
            index -= 1
        if not to_return_build or len(to_return_build) < 2: return default_to_return
        return to_return_build

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def ical_get_calendar_url(content, index, beg):
    URL = retrieve_element('ref=', content[index], 5, '<', "", 1, 0)
    if (beg == ""): return URL
    return beg + URL

def ical_get_content(URL, is_broken, school_name):
    response = urllib2.urlopen(str(URL)).read()
    
    if (is_broken):
        #classname.fix_ics
        exec("response = " + school_name +"_fix_ics(response)")
    content = Calendar.from_ical(response)
    return content

def uwash_fix_ics(response):
    removed_file = 0
    for line in Contentlines.from_ical(response):
        if ((not removed_file) and os.path.exists("uwash.ics")):
            os.remove('uwash.ics')
            removed_file = 1
            
        if line.find("X-WR-$CALNAME") != -1:
            with open("uwash.ics","a+") as f:
                f.write('X-WR-CALNAME:UW CSE Colloquium Calendar\n')
                continue
        with open("uwash.ics","a+") as f:
            #print "HERE"
            f.write(line.encode("utf-8"))
            f.write('\n')
    content = open('uwash.ics').read()
    return content

def ical_get_content_from_url(content, index, beg, is_broken, school_name):
    return ical_get_content(ical_get_calendar_url(content, index, beg), is_broken, school_name)

def add_to_all_records(record):
    global all_records
    #for record in records:
    all_records.append(record)

def add_to_date_count(val):
    global date_count

    now = datetime.datetime.now()
    cur_year = now.year

    Year = val[:4]
    if(str(cur_year) != Year): return

    Month = val[5] + val[6]
    if(Month[0] == '0'):
        Month = Month[1]

    date_count[int(Month)] += 1

def normalize_metadata(metadata):
    count = 0
    for elt in metadata:
        if elt.isalpha():
            break
        count += 1
    metadata = metadata[count:]  
    return metadata

#deserializes the file and adds the records to all_records
#creates a new map of pairs<speaker,topic>, to distinguish between new and old colloquia
def deserialize(filePath):
    global speaker_date
    global all_records
    global date_count

    data = dict()
    with open(filePath, 'r') as f:
        data = json.load(f)
    f.close()

    speaker_date = []
    all_records = []
    for record in data["records"]:
        speaker_date_key = ""
        for key, value in record.iteritems():
            if (key == "Speaker"):
                speaker_date_key = value
            elif (key == "Time"):
                speaker_date_key = speaker_date_key + value
                add_to_date_count(str(value))
                speaker_date.append(speaker_date_key)
        add_to_all_records(record)


def serialize(filePath, SSS):
    global speaker_date
    global all_records
    
    for school in SSS.get_school_data().itervalues():
        for colloquia in school.get_colloquim():
            new_rec = create_record(colloquia.topic, colloquia.speaker, colloquia.date, colloquia.venue, colloquia.university, colloquia.url, colloquia.description, colloquia.tags)
            speaker_date_key = colloquia.speaker + str(colloquia.date)
            if speaker_date_key not in speaker_date:
                add_to_date_count(str(colloquia.date))
                add_to_all_records(new_rec)
    speaker_date = []

def write_tsv_file(tsv_filePath):
    global date_count
    date_count_file = open(tsv_filePath, 'w+')
    date_count_file.write('month\tcount\n')
    now = datetime.datetime.now()
    cur_year = str(now.year)

    index = 0
    for elt in date_count:
        index += 1
        if(elt == 0): continue
        new_elt = cur_year + "-" + str(index) + "\t" + str(elt) + "\n"
        date_count_file.write(new_elt)
    date_count_file.close()

def writeToFile_JSON(SSS, fileName):
    global speaker_date
    global all_records
    
    to_send = dict()
    
    working_dir = 'data'
    filePath = working_dir + '/' + fileName
    if(os.path.isfile(filePath)):
        deserialize(filePath)

    serialize(filePath, SSS)

    to_send["records"] = all_records    
    with open(filePath, 'w') as fout:
        json.dump(to_send, fout)
    fout.close()

    tsv_filePath = working_dir + '/' + 'month_total.tsv'
    write_tsv_file(tsv_filePath)

    """
    #For Debugging
    count = 0
    for record in all_records:
        for key, value in record.iteritems():
            if key == "Tags":
                print "TAGS_" + str(count) + ": "
                print value
                count += 1
    """