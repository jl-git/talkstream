from bs4 import BeautifulSoup
import dateutil.parser
import urllib2
import sys

URL='https://icme.stanford.edu/events/cme510-linear-algebra-and-optimization-seminar-1'

def scrape_icme(url, fbase):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)

    try:
        field_items = soup.find_all('div', class_='field-item')
        title = field_items[6].get_text()
        speaker = field_items[7].get_text()
        affiliation = field_items[8].get_text()
        date = field_items[9].get_text()
        d = dateutil.parser.parse(date, fuzzy=True)
    except:
        print "Could not parse {0}".format(url)
        return
    
    dd = d.date().isoformat()
    with open("{0}-{1}.md".format(dd, fbase), 'w') as f:
        f.write('---\n')
        f.write('Title: "{0}"\n'.format(title))
        f.write('Speaker: "{0}"\n'.format(speaker))
        f.write('Affiliation: "{0}"\n'.format(affiliation))
        f.write("Date: {0}\n".format(d))
        f.write("url: {0}\n".format(url))
        f.write("---\n")
        for p in field_items[0].find_all('p'):
            f.write(p.get_text().encode('utf-8'))
            f.write("\n\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
	for url in sys.argv[1:]:
	    scrape_icme(sys.argv[1], "stanford-cme510")
