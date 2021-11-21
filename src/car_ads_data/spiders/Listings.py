import scrapy

class ListingsSpider(scrapy.Spider):
    name = 'Listings'
    allowed_domains = ['www.carsales.com.au/cars/']
    start_urls = ['www.carsales.com.au/cars/']

    def parse(self, response):
        pass
