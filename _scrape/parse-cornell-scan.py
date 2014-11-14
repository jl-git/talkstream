#!/usr/local/bin/python

from bs4 import BeautifulSoup
import dateutil.parser
import urllib2
import sys
import string
import re
from talkrec import TalkRecord

def pack_ws(s):
    return re.sub(r"(\s+)", " ", s.strip())

def pack_pars(s):
    s = re.sub(r"^[ ]*", "", s)
    s = re.sub(r"([ ]*\n[ ]*)", "\n", s)
    return s

def scrape_date(soup):
    d = soup.find('th').get_text().encode('utf8')
    d = "{0}, 2014 13:25:00".format(d)
    d = dateutil.parser.parse(d, fuzzy=True)
    return d

def scrape_speaker(soup):
    return pack_ws(soup.find('td').get_text().encode('utf8'))

def scrape_title(soup):
    return pack_ws(soup.find_all('td')[1].get_text().encode('utf8'))

def scrape_url(soup):
    link = soup.find_all('td')[1].find('a')
    if link:
        return "http://www.math.cornell.edu/~scan/{0}".format(link.get('href'))
    return ''

def scrape_blurb(url):
    if not re.match(".*[.]html", url):
        return ''
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    soup = soup.find("div", class_="container")
    pars = soup.find_all('p')
    blurb = ''
    for p in pars:
        if p.string:
            blurb = blurb + pack_pars(p.string) + "\n"
    return blurb

def scrape(html, filter=r".*"):
    soup = BeautifulSoup(html)
    tbl = soup.find_all('tr')
    for tr in tbl[1:]:

        rec = TalkRecord()
        rec.series = "cornell-scan"
        rec.datetime = scrape_date(tr)
        if not re.match(filter, rec.date()):
            continue
        
        rec.speaker = scrape_speaker(tr)
        rec.title = scrape_title(tr)
        rec.url = scrape_url(tr)
        rec.blurb = scrape_blurb(rec.url)
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
        main("http://www.math.cornell.edu/~scan")
    elif len(sys.argv) == 2:
        mainf(sys.argv[1])
    elif len(sys.argv) > 2:
        mainf(sys.argv[1], sys.argv[2])
