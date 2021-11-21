import scrapy

class CarListingItemsSpider(scrapy.Spider):
    name = 'car-ad'
    start_urls = [
        'https://www.carsales.com.au/cars/?q=(And.Service.CARSALES._.(C.State.Western%20Australia._.Region.Perth.)_.Price.range(..20000)._.Odometer.range(..60000)._.Year.range(2015..)._.GenericGearType.Automatic._.Condition.Used.)',
    ]

    def parse(self, response):
        
        for car_ad in response.css('div.listing-item'):
            card_body = car_ad.css('div.card-body')
            key_details = card_body.css('ul.key-details')

            yield {
                # Details on class="listing-item" card element
                'id': car_ad.xpath('@id').get(),
                'vehcategory': car_ad.xpath('@data-webm-vehcategory').get(),
                'bodystyle': car_ad.xpath('@data-webm-bodystyle').get(),
                'make': car_ad.xpath('@data-webm-make').get(),
                'model': car_ad.xpath('@data-webm-model').get(),
                'state': car_ad.xpath('@data-webm-state').get(),
                'price': car_ad.xpath('@data-webm-price').get(),
                # Get the URL and title of listing
                'url': card_body.xpath('.//a/@href').get(),
                'title': card_body.xpath('.//a/text()').get(),
                # Get the odometer and other key details
                'odometer': key_details.xpath('//li[@data-type="Odometer"]/text()').get(),
                'transmission': key_details.xpath('//li[@data-type="Transmission"]/text()').get(),
                'engine': key_details.xpath('//li[@data-type="Engine"]/text()').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()

        if next_page is not None:
            yield response.follow(next_page, self.parse)