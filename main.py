from wanted.spiders import sarmain
from saramin.spiders import wanted
from scrapy.crawler import CrawlerProcess
from datetime import datetime
import logging

now = str(datetime.now().strftime('%Y_%m_%d_%H%M%S'))
        
logging.basicConfig(filename=f'./log/{now}.log', level=10)
process = CrawlerProcess()

logging.info('='*30)
logging.info("====="*10 +"Start! crawling "+"="*10)
logging.info('='*30)

process.crawl(sarmain)
process.crawl(wanted)
process.start()



