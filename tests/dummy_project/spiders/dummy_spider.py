import datetime as dt

import scrapy


class DummySpiderSpider(scrapy.Spider):
    name = "dummy_spider"
    allowed_domains = ["example.com"]
    start_urls = ["http://example.com/"]

    def parse(self, response):
        yield {"timestamp": dt.datetime.now(), "url": response.url}
