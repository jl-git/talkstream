#!/usr/local/bin/python

from bs4 import BeautifulSoup
import dateutil.parser
import urllib2
import sys
import string
import re
from talkrec import TalkRecord

URL="http://www.cs.nyu.edu/webapps/nasc_seminars"

def pack_ws(s):
    return re.sub(r"(\s+)", " ", s.strip())

def scrape_date(soup):
    d = soup.get_text().encode('utf8')
    d = "{0} 10:00:00".format(d)
    d = dateutil.parser.parse(d, fuzzy=True)
    return d

def scrape(html, filter=r".*"):
    soup = BeautifulSoup(html)
    tbl = soup.find('table', class_='listing')
    trs = tbl.find_all('tr')
    for tr in trs[1:]:
        tds = tr.find_all('td')
        rec = TalkRecord()
        rec.series = "nyu-nasc"
        rec.datetime = scrape_date(tds[0])
        if not re.match(filter, rec.date()):
            continue
        rec.speaker = pack_ws(tds[1].get_text().encode("utf8"))
        rec.title = pack_ws(tds[2].get_text().encode("utf8"))
        link = tds[2].find('a')
        if link:
            rec.url = "http://www.cs.nyu.edu/{0}".format(
                pack_ws(link.get('href')))
        rec.write()

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
