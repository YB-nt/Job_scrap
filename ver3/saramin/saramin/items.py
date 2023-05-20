# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



# class SaraminItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     # title = scrapy.Field()
#     # requirements = scrapy.Field()
#     job_num = scrapy.Field()
#     summary_link = scrapy.Field()
#     text = scrapy.Field()


class SaraminItem_info(scrapy.Item):
    id = scrapy.Field()
    platform = scrapy.Field()
    담당업무 = scrapy.Field()
    자격요건 = scrapy.Field()
    우대사항 = scrapy.Field()
    근무조건 = scrapy.Field()
    전형절차 = scrapy.Field()
    접수기간_및_방법 = scrapy.Field()


    