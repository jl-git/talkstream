import datetime
import json

class TalkDB(object):

    def __init__(self, fname):
        self.fname = fname
        try:
            with open(fname, 'r') as f:
                self.data = json.load(f)
        except:
            self.data = {}

    def save(self):
        with open(self.fname, 'w') as f:
            json.dump(self.data, f)
            
    def check(self, talk_tag):
        if talk_tag in self.data:
            return True
        else:
            return False

    def add(self, talk_tag):
        self.data[talk_tag] = datetime.date.today().isoformat()

    def rm(self, talk_tag):
        del self.data[talk_tag]
