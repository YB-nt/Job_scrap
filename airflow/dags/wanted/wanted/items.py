# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WantedItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    담당업무 = scrapy.Field()
    자격요건 = scrapy.Field()
    우대사항 = scrapy.Field()
    
