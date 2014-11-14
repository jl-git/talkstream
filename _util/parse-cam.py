#!/usr/local/bin/python

from bs4 import BeautifulSoup
import dateutil.parser
import urllib2
import sys
import string
import re

def write(title, speaker, date, url, blurb):
    with open('{0}-cornell-cam.md'.format(date), "w") as f:
        f.write('---\n')
        f.write('Title: "{0}"\n'.format(title))
        f.write('Speaker: {0}\n'.format(speaker))
        f.write("Date: {0} 13:25:00\n".format(date))
        f.write("url: {0}\n".format(url))
        f.write("series: cornell-cam\n")
        f.write("---\n\n")
        f.write(blurb)

def writes(title, speaker, date, url, blurb):
    print '---'
    print 'Title: "{0}"'.format(title)
    print 'Speaker: {0}'.format(speaker)
    print "Date: {0} 13:25:00".format(date)
    print "url: {0}".format(url)
    print "series: cornell-cam\n"
    print "---\n"
    print blurb.encode('utf-8')
            
def scrape(html):
    soup = BeautifulSoup(html)
    dates = soup.find_all('h4', class_='day-header')
    for daterec in dates:
        
        # -- Grab date
        d = daterec.get_text()
        d = re.sub("([\d ]+)", "", d, 1)
        d = dateutil.parser.parse(d, fuzzy=True)
        date = d.date().isoformat()
        print(date)

        rec = daterec.find_next_sibling('h5')
        if not rec:
            continue
        
        # -- Parse author, title
        rectxt = rec.get_text().encode("utf8").strip()
        fields = string.split(rectxt, ":")
        speakertitle = string.join(fields[1:], ":")
        fields = string.split(speakertitle, " - ")
        speaker = fields[0].strip()
        title = string.join(fields[1:], " - ").strip()

        # -- Get URL
        link = rec.find('a')
        url = ''
        if link:
            url = link.get('href')
        if not re.match("http", url):
            url = ''
        else:
            response = urllib2.urlopen(url)
            blurbhtml = response.read()
            blurbsoup = BeautifulSoup(blurbhtml).find('div', class_='description')
            blurb = blurbsoup.get_text().encode("utf8")
            blurb = re.sub("\n", "\n\n", blurb)
            
        write(title, speaker, date, url, blurb)
        
def main(url):
    response = urllib2.urlopen(url)
    html = response.read()
    scrape(html)

def mainf(url):
    with open(url, 'r') as f:
        html = f.read()
    scrape(html)
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        for url in sys.argv[1:]:
            mainf(sys.argv[1])
    else:
        URL='http://www.cam.cornell.edu/news/colloquium.cfm'
        main(URL)
