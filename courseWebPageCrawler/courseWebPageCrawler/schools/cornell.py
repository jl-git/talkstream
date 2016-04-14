import courseWebPageSpider
import shared
import os
import re
import urlparse
import json

global topic_count
global records
#record to insert in array of dict, 'records'
topic_count = 1

#Records
records = [dict()]


def UST_extractor(elt, num):
    global topic_count

    if (num == 2):
        index_speaker = elt.index('<a href=') + 9
        URL = ''
        while(elt[index_speaker] != '"'):
            URL += elt[index_speaker]
            index_speaker += 1
        #print URL

        index_speaker += 2
        Speaker = ''
        while(elt[index_speaker] != '<'):
            Speaker += elt[index_speaker]
            index_speaker += 1
        #print Speaker
        
        records[topic_count]['URL'] = URL.encode("utf-8")
        records[topic_count]['Speaker'] = Speaker.encode("utf-8")
        topic_count += 1
    
    elif (num == 1):

        index_topic = elt.index('<em>') + 4
        Topic = ''
        href_found = 0
        #print elt[index_topic]
        if(elt[index_topic] == '<'):
            href_found = 1
            while(elt[index_topic] != '>'):
                index_topic += 1
        #index_topic += 1
        if href_found == 1:
            while(elt[index_topic] != '<'):
                Topic += elt[index_topic]
                index_topic += 1
            #print Topic
            records[topic_count]['Topic'] = Topic.encode("utf-8")
            return

        while(elt[index_topic] != '<'):
            Topic += elt[index_topic]
            index_topic += 1
        #print Topic
        #records[topic_count]['URL'] = URL ---> Design Choice
        records[topic_count]['Topic'] = Topic.encode("utf-8")
        if "Speaker" in elt:
            index = elt.index('Speaker') + 18
            URL = ''
            while (elt[index] != '"'):
                URL += elt[index]
                index += 1
            #print URL
            records[topic_count]['URL'] = URL.encode("utf-8")
            index += 2
            Speaker = ''
            while (elt[index] != '<'):
                Speaker += elt[index]
                index += 1
            #print Speaker
            records[topic_count]['Speaker'] = Speaker.encode("utf-8")

            topic_count += 1
          
def speaker_topic_url_handler(h4):
    global topic_count
    count = 0

    prev_tag = ""
    for elt in h4:
        count += 1
        #print str(count) + " " + elt
        if len(elt) < 12:
            continue
        elif "TBD" in elt:
           # print "FOUND TBD" + '\n'
            records[topic_count]['Topic'] = "Topic/Title TBD"
            prev_tag = "TBD"
        elif "No Colloquium" in elt:
            #print "FOUND NO Colloquium" + '\n'
            #CLEAN THESE OUT
            records[topic_count]['Topic'] = "NO"
            topic_count += 1
            prev_tag = "NoC"
        elif ("<em>" in elt):

            if prev_tag != 'Title':
                UST_extractor(elt, 1)
            prev_tag = "Title"

        elif (("Speaker:" in elt) or ('"speaker"' in elt)):
            #print "FOUND Speaker:" + '\n'
            if prev_tag == "TBD" or prev_tag == "Title":
                UST_extractor(elt, 2)
            prev_tag = "Speaker" 


def clean_no_colloqiums():
    not_first = 0
    for record in list(records):
        if not_first:
            if record['Topic'] == 'NO':
                records.remove(record)
        else:
            records.remove(record)
        not_first += 1

