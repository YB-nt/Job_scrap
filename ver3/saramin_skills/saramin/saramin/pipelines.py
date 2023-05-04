# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from saramin.items import SaraminItem_info#,SaraminItem
import json
import pymongo



class SaraminPipeline:
    def __init__(self):
        self.info_file = open("./data/saramin_info.json", "w", encoding="utf-8")
    
    def open_spider(self, spider):
        self.info_file = open("./data/saramin_info.json", "w", encoding="utf-8")

    def close_spider(self, spider):
        self.info_file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.info_file.write(line)
        return item


class MongoDBPipeline(object):
    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection
        self.mongo_uri = mongo_uri
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGODB_URI'),
            mongo_db=crawler.settings.get('MONGODB_DB'),
            mongo_collection=crawler.settings.get('MONGODB_COLLECTION')
        )
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)  
        self.db = self.client[self.mongo_db]
    
    def close_spider(self, spider):
        self.client.close()
    
    def process_item(self, item, spider):
        try:
            self.db[self.mongo_collection].insert(dict(item))
        except: 
            try:
                self.db[self.mongo_collection].insert_one(dict(item))
                
            
            except Exception as e:
                print("="*100)
                print("="*100)
                print(e)
                print("="*100)
                print("="*100)
                with open('./data/except_saramin.json', 'a') as f:
                    f.write(json.dumps(dict(item)) + '\n')
        return item
        

# class JsonWriterPipeline(object):
#     def open_spider(self, spider):
#         self.file = open('./data/item1.json', 'w')
    
#     def close_spider(self, spider):
#         self.file.close()
    
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.file.write(line)
#         return item
