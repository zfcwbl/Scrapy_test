# -*- coding: utf-8 -*-
import scrapy
class DoubanmovieItem(scrapy.Item):
    #定义需要获取的信息
    rank = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    rate = scrapy.Field()
    quote = scrapy.Field()
