
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CourseWebPage(Item):
    name = Field()
    description = Field()
    url = Field()
    school_name = Field()
    url_to_school = Field()

    topic = Field()
    speaker = Field()
    time = Field()
    venue = Field()
    uni = Field()
    tags = Field()