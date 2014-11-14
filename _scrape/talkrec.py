#!/usr/local/bin/python

class TalkRecord(object):

    def __init__(self):
        self.title = None
        self.speaker = None
        self.datetime = None
        self.url = None
        self.series = None
        self.blurb = None

    def date(self):
        if self.datetime:
            return self.datetime.date().isoformat()
        return ''
    
    def write(self):
        with open('{0}-{1}.md'.format(self.date(), self.series), "w") as f:
            f.write('---\n')
            if self.title:
                f.write('Title: "{0}"\n'.format(self.title))
            if self.speaker:
                f.write('Speaker: {0}\n'.format(self.speaker))
            if self.datetime:
                f.write("Date: {0}\n".format(self.datetime))
            if self.url:
                f.write("url: {0}\n".format(self.url))
            if self.series:
                f.write("series: {0}\n".format(self.series))
            f.write("---\n")
            if self.blurb:
                f.write(self.blurb)

    def writes(self):
        print '--- {0}-{1}.md ---'.format(self.date(), self.series)
        if self.title:
            print 'title: "{0}"'.format(self.title)
        if self.speaker:
            print 'speaker: {0}'.format(self.speaker)
        if self.datetime:
            print "date: {0}".format(self.datetime)
        if self.url:
            print "url: {0}".format(self.url)
        if self.series:
            print "series: {0}".format(self.series)
        print "---"
        if self.blurb:
            print self.blurb
