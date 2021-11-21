scrape-car-sales
==============================

Tools to scrape details published in carsales.com.au and saved them on a data store.

To run the spider generated on that project and save the results on a JSON file:
```
cd src
scrapy crawl car-ad -O car-ads_YYYYMMDD.json
```

# Initialise scrapy project

The following commands will initialise the project and create a basic spider:

```
cd src
scrapy startproject car_ads_data
scrapy genspider Listings https://www.carsales.com.au/cars/
```



# Use Shell to test spider
> NOTE: Use double quotations in Windows
```
scrapy shell "https://www.carsales.com.au/cars/"
```
