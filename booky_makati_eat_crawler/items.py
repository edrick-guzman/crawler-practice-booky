# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookyMakatiEatCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    URL = scrapy.Field()
    Name = scrapy.Field()
    Address = scrapy.Field()
    Category = scrapy.Field()
    Coordinates = scrapy.Field()
    Deal = scrapy.Field()
    Image_url = scrapy.Field()
