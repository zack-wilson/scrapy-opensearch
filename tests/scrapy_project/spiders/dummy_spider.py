import datetime as dt
import uuid

import scrapy


class DummySpiderSpider(scrapy.Spider):
    name = "dummy_spider"
    allowed_domains = ["example.com"]
    start_urls = ["http://example.com/"]

    def parse(self, response):
        yield {
            "uuid": uuid.uuid1().hex,
            "timestamp": dt.datetime.now(),
            "url": response.url,
            "title": response.css("title").get(),
        }
