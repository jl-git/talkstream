#!/usr/local/bin/python

from bs4 import BeautifulSoup
import dateutil.parser
import urllib2
import sys
import string
import re
import textwrap
from talkrec import TalkRecord

def pack_ws(s):
    return re.sub(r"(\s+)", " ", s.strip())

def pack_pars(s):
    s = re.sub(r"^[ ]*", "", s)
    s = re.sub(r"([ ]*\n[ ]*)", "\n", s)
    return s

def scrape_date(soup):
    d = soup.get_text().encode('utf8').encode("utf8").strip()
    p = re.compile(".*\n.*[,](.*)")
    m = p.match(d)
    d = "{0} 15:30:00".format(m.group(1))
    d = dateutil.parser.parse(d, fuzzy=True)
    return d

def scrape_blurb(url):
    if not re.match("http:", url):
        return ''
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    soup = soup.find("div", class_="description")
    pars = soup.find_all('p')
    blurb = '\n'
    for p in pars:
        if p.string:
            blurb = blurb + pack_pars(p.string.encode("utf8")) + "\n\n"
    return blurb

def scrape(html, filter=r".*"):
    soup = BeautifulSoup(html)
    dates = soup.find_all('h4')
    patt1 = re.compile("\s*[^:]*:(.*\(.*\))\s*-\s*([^\n]*)")
    for date in dates:
        rec = TalkRecord()
        rec.series = "cornell-cam"
        rec.datetime = scrape_date(date)
        if not re.match(filter, rec.date()):
            continue
        infos = date.find_next_sibling('h5')
        if not infos:
            continue
        m = patt1.match(infos.get_text().encode("utf8"))
        if not m:
            continue
        rec.speaker = m.group(1)
        rec.title = m.group(2)
        rec.url = infos.find('a').get('href')
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
        main("http://www.cam.cornell.edu/news/colloquium.cfm")
    elif len(sys.argv) == 2:
        mainf(sys.argv[1])
    elif len(sys.argv) > 2:
        mainf(sys.argv[1], sys.argv[2])
