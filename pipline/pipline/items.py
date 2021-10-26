# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PiplineItem(scrapy.Item):
    # define the fields for your item here like:
    check = scrapy.Field()
    date = scrapy.Field()
    system =scrapy.Field()
    angle =scrapy.Field()
    utilization_rate =scrapy.Field()
    weekJumpRatio =scrapy.Field()
    jump =scrapy.Field()
    l1 =scrapy.Field()
    l2 =scrapy.Field()
    l5 =scrapy.Field()
    e5 =scrapy.Field()
    e6 =scrapy.Field()
    mp1 =scrapy.Field()
    mp2 =scrapy.Field()
    mp3 =scrapy.Field()
    mp4 =scrapy.Field()
    mp5 =scrapy.Field()
