# Initialise scrapy project

The following commands will initialise the project and create a basic spider:

```
cd src
scrapy startproject car_ads_data
scrapy genspider Listings https://www.carsales.com.au/cars/
```

To run the spider generated on that project:
```
scrapy crawl Listings
```

# Use Shell to test spider
> NOTE: Use double quotations in Windows
```
scrapy shell "https://www.carsales.com.au/cars/"
```