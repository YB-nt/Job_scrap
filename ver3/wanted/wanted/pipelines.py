# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo,json,re


class WantedPipeline:
    # def __init__(self): 
    #     self.info_file = open("./data/wanted.json", "w", encoding="utf-8")
    
    # def open_spider(self, spider):
    #     self.info_file = open("./data/wanted.json", "w", encoding="utf-8")

    # def close_spider(self, spider):
    #     self.info_file.close()
    """
    담당업무 = scrapy.Field()
    자격요건 = scrapy.Field()
    우대사항 = scrapy.Field()
    전형절차 = scrapy.Field()
    접수기간_및_방법 = scrapy.Field()
    """
    def process_item(self, item, spider):
        if item['담당업무']:
            item['담당업무'] = re.sub(r'담당업무|주요업무','',item['담당업무'])
            item['담당업무'] = item['담당업무'].strip()
            item['담당업무'] = re.sub(r'\s',' ',item['담당업무'])
        if item['자격요건']:
            item['자격요건'] = re.sub(r'자격요건|지원자격|지원요건|근무조건','',item['자격요건'])
            item['자격요건'] = item['자격요건'].strip()
            item['자격요건'] = re.sub(r'\s',' ',item['자격요건'])
        if item['우대사항']:
            item['우대사항'] = re.sub(r'우대사항','',item['우대사항']) 
            item['우대사항'] = re.sub(r'\s',' ',item['우대사항'])
            item['우대사항'] = item['우대사항'].strip()
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
        item_id = item.get('id')
        if self.collection.count_documents({'id':item_id}) > 0:
            return item
        else:
            try:
                self.db[self.mongo_collection].insert(dict(item))
            except: 
                try:
                    self.db[self.mongo_collection].insert_one(dict(item))
                    
                except Exception as e:
                    print(e) 
                    with open('./data/except_wanted.json', 'a') as f:
                        f.write(json.dumps(dict(item)) + '\n')

        return item
        
