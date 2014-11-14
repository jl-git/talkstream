import dateutil.parser
import urllib2
import json
import string
import re

from talkdb import TalkDB

API="https://www.kimonolabs.com/api/8zu62nzq?apikey=p7uaht6sJR2Ni0jKPODwSLmUT99KjEyT"

response = urllib2.urlopen(API)
data = json.loads(response.read())
talkdb = TalkDB("talks.json")

def pack_ws(s):
    return re.sub("(\s|\\n)+", " ", s)

for rec in data['results']['collection1']:
    speaker = pack_ws(rec['Speaker']['text'])
    d = "{0} 15:00:00".format(rec['Date'])
    try:
        d = dateutil.parser.parse(d, fuzzy=True)
        fname = "{0}-ncsu-amc.md".format(d.date().isoformat())
        if talkdb.check(fname):
            print "Already recorded {0}".format(fname)
            continue
        talkdb.add(fname)
        print "Generate {0}".format(fname)
        with open(fname, 'w') as f:
            f.write("---\n")
            f.write("title: {0}\n".format(rec['Title']['text']))
            f.write("speaker: {0}\n".format(speaker))
            f.write("speaker-url: {0}\n".format(rec['Speaker']['href']))
            f.write("affil: \n")
            f.write("date: {0}\n".format(d))
            f.write("talk-url: {0}\n".format(rec['Title']['href']))
            f.write("series: ncsu-amc\n")
            f.write("---\n")
    except:
        print "... Skip invalid date {0} ...".format(rec['Date'])
    

talkdb.save()
