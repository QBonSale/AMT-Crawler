# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class MturkItem(Item):
    # define the fields for your item here like:
    # name = Field()
    groupid = Field()
    requester = Field()
    title = Field()
    description = Field()
    keywords = Field()
    rewards = Field()
    number_of_HITs_available = Field()
    qualifications_required = Field()
    time_of_expiration = Field()
    expected_minutes_cost = Field()
    collected_time = Field()
