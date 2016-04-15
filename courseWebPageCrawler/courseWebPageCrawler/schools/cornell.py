import os
import re
import urlparse
import json
import datetime

from ..classes.sss import SSS
from ..classes.shared import extract_html
from ..classes.shared import days

global topic_count
topic_count = 0

def cornell_executor(my_SSS):
    #get school object stored for respective school from SSS(Super Seminar Scraper)
    school = my_SSS.get_school('cornell')
    #content_list is all h2s
    my_SSS.extract_content(school.get_name(), "//h2")
    #filtered_content is same as content_list
    my_SSS.filter_content(school.get_name(), days)
    
    #get the dates from there
    my_SSS.retrieve_dates(school.get_name(), "Day", 1)

    my_SSS.set_filtered_content(extract_html(my_SSS, 'cornell', "//h4"), 'cornell')

    #highly special scraper for cornell's disorganized website
    speaker_topic_url_handler(my_SSS.get_filtered_content(), my_SSS)

    #Set Venue and Official School Name Manually from the school object
    school.set_venue("G01 Gates Hall - Mentor's Lecture Hall")
    school.set_official_name("Cornell University")

def speaker_topic_url_handler(h4, my_SSS):
    global topic_count
    count = 0
    prev_tag = ""
    for elt in h4:
        count += 1
        if len(elt) < 12:
            continue
        elif "TBD" in elt:
            my_SSS.get_school('cornell').get_colloquim()[topic_count].set_metadata('topic', "Topic/Title TBD")
            prev_tag = "TBD"
        elif "No Colloquium" in elt:
            my_SSS.get_school('cornell').get_colloquim()[topic_count].set_metadata('topic', "NO")
            topic_count += 1
            prev_tag = "NoC"
        elif ("<em>" in elt):

            if prev_tag != 'Title':
                UST_extractor(elt, 1, my_SSS)
            prev_tag = "Title"

        elif (("Speaker:" in elt) or ('"speaker"' in elt)):
            if prev_tag == "TBD" or prev_tag == "Title":
                UST_extractor(elt, 2, my_SSS)
            prev_tag = "Speaker" 
    clean_no_colloqiums(my_SSS)    

def UST_extractor(elt, num, my_SSS):
    global topic_count

    if (num == 2):
        index_speaker = elt.index('<a href=') + 9
        URL = ''
        while(elt[index_speaker] != '"'):
            URL += elt[index_speaker]
            index_speaker += 1

        index_speaker += 2
        Speaker = ''
        while(elt[index_speaker] != '<'):
            Speaker += elt[index_speaker]
            index_speaker += 1

        my_SSS.get_school('cornell').get_colloquim()[topic_count].set_metadata('url', URL.encode("utf-8"))
        my_SSS.get_school('cornell').get_colloquim()[topic_count].set_metadata('speaker', Speaker.encode("utf-8"))
        topic_count += 1
    
    elif (num == 1):

        index_topic = elt.index('<em>') + 4
        Topic = ''
        href_found = 0
        if(elt[index_topic] == '<'):
            href_found = 1
            while(elt[index_topic] != '>'):
                index_topic += 1
        if href_found == 1:
            while(elt[index_topic] != '<'):
                Topic += elt[index_topic]
                index_topic += 1
            my_SSS.get_school('cornell').get_colloquim()[topic_count].set_metadata('topic', Topic.encode("utf-8"))
            return

        while(elt[index_topic] != '<'):
            Topic += elt[index_topic]
            index_topic += 1

        my_SSS.get_school('cornell').get_colloquim()[topic_count].set_metadata('topic', Topic.encode("utf-8"))

        if "Speaker" in elt:
            index = elt.index('Speaker') + 18
            URL = ''
            while (elt[index] != '"'):
                URL += elt[index]
                index += 1
            my_SSS.get_school('cornell').get_colloquim()[topic_count].set_metadata('url', URL.encode("utf-8"))
            index += 2
            Speaker = ''
            while (elt[index] != '<'):
                Speaker += elt[index]
                index += 1
            my_SSS.get_school('cornell').get_colloquim()[topic_count].set_metadata('speaker', Speaker.encode("utf-8"))
            topic_count += 1

def clean_no_colloqiums(my_SSS):

    for elt in list(my_SSS.get_school('cornell').get_colloquim()):
        if elt.topic == 'NO':
                my_SSS.get_school('cornell').get_colloquim().remove(elt)