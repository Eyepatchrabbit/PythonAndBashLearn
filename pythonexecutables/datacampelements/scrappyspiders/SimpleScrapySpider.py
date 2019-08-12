# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess


class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    # allowed_domains = ['quotes.toscrape.com']
    # start_urls = ['http://quotes.toscrape.com/']

    # start_requests method
    def start_requests(self):
        yield scrapy.Request(url='http://quotes.toscrape.com/',
                             callback=self.parse_def_made)

    # TODO: reqreate the pokemon method here!
    def parse_def_made(self, response):
        quotes = response.xpath('//*[@class="quote"]')

        for quote in quotes:
            text = quote.xpath(".//*[@class='text']/text()").extract_first()
            author = quote.xpath(".//*[@class='author']/text()").extract_first()
            tags = quote.xpath(".//*[@class='tag']/text()").extract()

            print('\n')
            print(text)
            print(author)
            print(tags)
            print("")


# Run the Spider
process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()
