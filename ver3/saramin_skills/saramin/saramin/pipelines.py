# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from saramin.items import SaraminItem_info,SaraminItem
import json
import pymongo



class SaraminPipeline:
    def __init__(self):
        self.file = open("./data/saramin_item.json", "w", encoding="utf-8")
        self.info_file = open("./data/saramin_info.json", "w", encoding="utf-8")
    def open_spider(self, spider):
        self.file = open("./data/saramin_item.json", "w", encoding="utf-8")
        self.info_file = open("./data/saramin_info.json", "w", encoding="utf-8")

    def close_spider(self, spider):
        self.file.close()
        self.info_file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        if isinstance(item, SaraminItem):
            self.file.write(line)
        elif isinstance(item, SaraminItem_info):
            self.info_file.write(line)

        return item


class MongoDBPipeline(object):
    def __init__(self, mongo_server, mongo_port, mongo_db, mongo_collection,mongo_user,mongo_password):
        self.mongo_user = mongo_user
        self.mongo_password = mongo_password
        self.mongo_server = mongo_server
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            uri = crawler.settings.get('URI'),
            mongo_db=crawler.settings.get('MONGODB_DB'),
            mongo_collection=crawler.settings.get('MONGODB_COLLECTION')
        )
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.uri)  
        self.db = self.client[self.mongo_db]
    
    def close_spider(self, spider):
        self.client.close()
    
    def process_item(self, item, spider):
        try:
            self.db[self.collection_name].insert(dict(item))
        except:
            with open('./data/except_saramin.json', 'a') as f:
                f.write(json.dumps(dict(item)) + '\n')
        return item
        

# class JsonWriterPipeline:
#     def __init__(self):
#         self.info_file = None
#         self.item_file = None
#         self.file = None

#     def open_spider(self, spider):
#         self.info_file = open('./data/saramin_info.json', 'w', encoding='utf-8')
#         self.item_file = open('./data/saramin_item.json', 'w', encoding='utf-8')

#     def process_item(self, item, spider):
#         if isinstance(item, SaraminItem_info):
#             line = json.dumps(dict(item), ensure_ascii=False) + '\n'
#             self.info_file.write(line)
#         elif isinstance(item, SaraminItem):
#             line = json.dumps(dict(item), ensure_ascii=False) + '\n'
#             self.item_file.write(line)

#         return item

#     def close_spider(self, spider):
#         self.info_file.close()
#         self.item_file.close()