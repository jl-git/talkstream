#!/usr/local/bin/python

from bs4 import BeautifulSoup
import dateutil.parser
import urllib2
import sys
import string
import re
from talkrec import TalkRecord

URL="http://www-math.mit.edu/amc/fall14/"

def pack_ws(s):
    return re.sub(r"(\s+)", " ", s.strip())

def scrape_date(soup):
    d = soup.get_text().encode('utf8').encode("utf8").strip()
    d = "{0}, 2014 16:30:00".format(d)
    d = dateutil.parser.parse(d, fuzzy=True)
    return d

def scrape(html, filter=r".*"):
    soup = BeautifulSoup(html)
    tbl = soup.find('table', class_='data')
    trs = tbl.find_all('tr')
    for j in range(1,len(trs)-1,2):
        tds1 = trs[j].find_all('td')    # Date and speaker
        tds2 = trs[j+1].find_all('td')  # Blank and abstract
        rec = TalkRecord()
        rec.series = "mit-amc"
        rec.datetime = scrape_date(tds1[0])
        if len(tds2) < 2:
            continue
        rec.speaker = tds1[1].get_text().encode("utf8")
        if not re.match(filter, rec.date()):
            continue
        rec.title = pack_ws(tds2[1].get_text().encode("utf8"))
        rec.url = "{0}{1}".format(URL, tds2[1].find('a').get('href'))
        if rec.title != '':
            rec.writes()

def main(url, filter=r".*"):
    response = urllib2.urlopen(url)
    html = response.read()
    html = re.sub("</br>", "<br/>", html)
    scrape(html)

def mainf(fname, filter=r".*"):
    with open(fname, 'r') as f:
        html = f.read()
    scrape(html, filter)
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        main(URL)
    elif len(sys.argv) == 2:
        mainf(sys.argv[1])
    elif len(sys.argv) > 2:
        mainf(sys.argv[1], sys.argv[2])
