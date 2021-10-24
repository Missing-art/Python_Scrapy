import scrapy


class DataSpider(scrapy.Spider):
    name = 'data'
    allowed_domains = ['www.xxxxx.com']
    start_urls = ['http://www.xxxxx.com/']

    def parse(self, response):
        pass
