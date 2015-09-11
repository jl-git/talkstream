#!/usr/local/bin/python

from bs4 import BeautifulSoup
import datetime
import urllib2
import sys
import string
import re
import yaml

DBFILE="simax.yml"
URL="http://epubs.siam.org/action/showFeed?ui=0&mi=3ezuvv&ai=s7&jc=sjmael&type=etoc&feed=rss"

def scrape(xml):

    # Grab old database and mark DOIs to avoid repeat records
    with open(DBFILE, 'r') as f:
        ydoc = yaml.safe_load(f)
    yset = frozenset([yrec['doi'] for yrec in ydoc])

    # Scrape the SIMAX RSS feed for information on new records
    soup = BeautifulSoup(xml)
    items = soup.find_all('rss:item')
    for item in items:
        title = item.find('rss:title')
        link = item.find('rss:link')
        doi = item.find('dc:identifier')
        date = item.find('dc:date')
        authors = date.next.next.encode("utf8")
        volume = item.find('prism:volume')
        pp_start = item.find('prism:startingpage')
        pp_end   = item.find('prism:endingpage')
        doitxt = doi.get_text().encode("utf8")
        if doitxt not in yset:
            print "Add: {0}".format(title.get_text().encode("utf8"))
            ydoc.append({
                'title': title.get_text().encode("utf8"),
                'authors': authors,
                'link': link.get_text().encode("utf8"),
                'doi': doi.get_text().encode("utf8"),
                'date': date.get_text().encode("utf8"),
                'volume': volume.get_text().encode("utf8"),
                'pp_start': pp_start.get_text().encode("utf8"),
                'pp_end': pp_end.get_text().encode("utf8")})

    # Sort all records and write updated database
    ydoc.sort(key=lambda rec: int(rec['volume'])*1e6 + int(rec['pp_start']))
    with open(DBFILE, 'w') as f:
        f.write('# Automatically generated from SIMAX RSS feed\n')
        f.write('# Last update: {0}\n\n'.format(datetime.datetime.now()))
        yaml.safe_dump(ydoc, stream=f, default_flow_style=False, encoding='utf-8', allow_unicode=True)

def main(url):
    response = urllib2.urlopen(url)
    xml = response.read()
    scrape(xml)

def mainf(fname):
    with open(fname, 'r') as f:
        xml = f.read()
    scrape(xml)
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        main(URL)
    elif len(sys.argv) == 2:
        mainf(sys.argv[1])
