# kallofem_scraper/items.py
import scrapy

class KallofemItem(scrapy.Item):
    product_name = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()