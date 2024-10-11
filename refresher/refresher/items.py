# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RefresherItem(scrapy.Item):
    # define the fields for your item here like:
    car_url = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    brand = scrapy.Field()
    year = scrapy.Field()
    body = scrapy.Field()
    body2 = scrapy.Field()
    odometer = scrapy.Field()
    interior_color = scrapy.Field()
    exterior_color = scrapy.Field()
    engine = scrapy.Field()
    transmission = scrapy.Field()
    fuel = scrapy.Field()
    description = scrapy.Field()

    
     
    