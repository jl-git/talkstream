import dateutil.parser
import urllib2
import json
import string
import re

from talkdb import TalkDB

API="https://www.kimonolabs.com/api/47cybuwu?apikey=p7uaht6sJR2Ni0jKPODwSLmUT99KjEyT"

response = urllib2.urlopen(API)
data = json.loads(response.read())
talkdb = TalkDB("talks.json")

def pack_ws(s):
    return re.sub("(\s|\\n)+", " ", s)

for rec in data['results']['collection1']:
    speaker = pack_ws(rec['speaker']['text'])
    month=rec['month-year'][0:3]
    year=rec['month-year'][5:10]
    d = "{0} {1}, {2} 15:00:00".format(month, rec['Day'], year)
    try:
        d = dateutil.parser.parse(d, fuzzy=True)
        fname = "{0}-manchester-nas.md".format(d.date().isoformat())
        if talkdb.check(fname):
            print "Already recorded {0}".format(fname)
            continue
        talkdb.add(fname)
        print "Generate {0}".format(fname)
        with open(fname, 'w') as f:
            f.write("---\n")
            f.write("title: {0}\n".format(rec['title']['text']))
            f.write("speaker: {0}\n".format(speaker))
            f.write("speaker-url: {0}\n".format(rec['speaker']['href']))
            f.write("affil: {0}\n".format(rec['affiliation']['text']))
            f.write("date: {0}\n".format(d))
            f.write("talk-url: {0}\n".format(rec['title']['href']))
            f.write("series: manchester-nas\n")
            f.write("---\n")
    except:
        print "... Skip invalid date {0} ({1} / {2})...".format(d, rec['month-year'], rec['Day'])
    

talkdb.save()
