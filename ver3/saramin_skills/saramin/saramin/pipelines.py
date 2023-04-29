# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from saramin.items import SaraminItem_info,SaraminItem
import json


class SaraminPipeline:
    def __init__(self):
        self.file = open("saramin_item.json", "w", encoding="utf-8")
        self.info_file = open("saramin_info.json", "w", encoding="utf-8")
    def open_spider(self, spider):
        self.file = open("saramin_item.json", "w", encoding="utf-8")
        self.info_file = open("saramin_info.json", "w", encoding="utf-8")

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




class JsonWriterPipeline:
    def __init__(self):
        self.info_file = None
        self.item_file = None
        self.file = None

    def open_spider(self, spider):
        self.info_file = open('saramin_info.json', 'w', encoding='utf-8')
        self.item_file = open('saramin_item.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(item, SaraminItem_info):
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.info_file.write(line)
        elif isinstance(item, SaraminItem):
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.item_file.write(line)

        return item

    def close_spider(self, spider):
        self.info_file.close()
        self.item_file.close()