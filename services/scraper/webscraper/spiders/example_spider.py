import scrapy
from datetime import datetime

class ExampleSpider(scrapy.Spider):
    name = "example_spider"
    start_urls = ["https://example.org"]

    def parse(self, response):
        yield {
            "url": response.url,
            "status": response.status,
            "timestamp": datetime.utcnow().isoformat(),
            "title": response.css("title::text").get(),
        }
