# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TribunnewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tag = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
   
