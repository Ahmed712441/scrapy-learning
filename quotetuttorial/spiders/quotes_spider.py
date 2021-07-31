import scrapy
from ..items import QuotetuttorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self,response):

        # title = response.css('title::text').extract()

        items = QuotetuttorialItem()
        quote = response.css('span.text::text').extract()
        author = response.css('small.author::text').extract()
        tags = response.css('div.tags')
        quote_tag = []

        for i  in range(len(tags)):

            items['tag'] = tags[i].css('a.tag::text').extract()

            # next_page = response.css('li.next a').xpath('@href').extract()

            items['author'] = author[i]
            items['quote'] = quote[i]


            yield items

        next_page = response.css('li.next a').xpath('@href').extract()

        if next_page is not None:
            yield response.follow(next_page[0],callback=self.parse)
