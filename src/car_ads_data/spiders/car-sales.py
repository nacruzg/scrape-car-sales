import scrapy

class CarListingItemsSpider(scrapy.Spider):
    name = 'car-ad'
    start_urls = [
        'https://www.carsales.com.au/cars/?q=(And.Service.CARSALES._.(C.State.Western%20Australia._.Region.Perth.)_.Price.range(..20000)._.Odometer.range(..60000)._.Year.range(2015..)._.GenericGearType.Automatic._.Condition.Used.)',
    ]

    def parse(self, response):
        
        for car_ad in response.css('div.listing-item'):
            
            yield {
                'author': car_ad.xpath('span/small/text()').get(),
                'text': car_ad.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()

        if next_page is not None:
            yield response.follow(next_page, self.parse)