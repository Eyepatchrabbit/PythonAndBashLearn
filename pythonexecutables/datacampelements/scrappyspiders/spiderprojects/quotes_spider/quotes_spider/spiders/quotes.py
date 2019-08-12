# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # base elements=>base spider lesson
        # h1tag = response.xpath("//h1/a/text()").extract_first()
        # tags = response.xpath("//*[@class='tag-item']/a/text()").extract()
        # yield {'H1Tag': h1tag, 'Tags': tags}
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
