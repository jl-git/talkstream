import dateutil.parser
import urllib2
import json
import string
import re

from talkdb import TalkDB

API="https://www.kimonolabs.com/api/730wcm2w?apikey=p7uaht6sJR2Ni0jKPODwSLmUT99KjEyT"

response = urllib2.urlopen(API)
data = json.loads(response.read())
talkdb = TalkDB("talks.json")

def pack_ws(s):
    return re.sub("(\s|\\n)+", " ", s)

patt = re.compile("(.*)\s+-\s+(.*)")
for rec in data['results']['collection1']:
    m = patt.match(rec['Speaker'])
    d = rec['Date']
    try:
        speaker = m.group(1)
        affil = m.group(2)
        d = dateutil.parser.parse(d, fuzzy=True)
        fname = "{0}-princeton-pacm.md".format(d.date().isoformat())
        if talkdb.check(fname):
            print "Already recorded {0}".format(fname)
            continue
        talkdb.add(fname)
        print "Generate {0}".format(fname)
        with open(fname, 'w') as f:
            f.write("---\n")
            f.write("title: {0}\n".format(rec['Title']['text']))
            f.write("speaker: {0}\n".format(speaker))
            f.write("speaker-url: \n")
            f.write("affil: {0}\n".format(affil))
            f.write("date: {0}\n".format(d))
            f.write("talk-url: {0}\n".format(rec['Title']['href']))
            f.write("series: princeton-pacm\n")
            f.write("---\n")
    except:
        print "... Skip invalid date {0} ...".format(rec['Date'])
    
talkdb.save()
