import scrapy

class ListingsSpider(scrapy.Spider):
    name = 'Listings'
    allowed_domains = ['https://www.carsales.com.au/cars/']
    start_urls = ['http://https://www.carsales.com.au/cars//']

    def parse(self, response):
        pass
