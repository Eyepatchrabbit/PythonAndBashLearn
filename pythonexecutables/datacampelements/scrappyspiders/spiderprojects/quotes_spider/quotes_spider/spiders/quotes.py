# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        h1tag = response.xpath("//h1/a/text()").extract_first()
        tags = response.xpath("//*[@class='tag-item']/a/text()").extract()

        yield {'H1Tag': h1tag, 'Tags': tags}
