# -*- coding: utf-8 -*-
import scrapy
class DoubanmovieItem(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    rate = scrapy.Field()
    quote = scrapy.Field()
