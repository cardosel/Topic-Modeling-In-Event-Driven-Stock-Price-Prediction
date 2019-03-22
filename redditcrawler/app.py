
"""Script to crawl Top Posts across sub reddits and store results in MongoDB
    """

import logging
import time
import datetime
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from redditcrawler.spiders import PostSpider
from scrapy.utils.project import get_project_settings
from scrapy.xlib.pydispatch import dispatcher

result = None
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def set_result(item):
    result = item

while True:
    process = CrawlerProcess(get_project_settings())
    dispatcher.connect(set_result, signals.item_scraped)

    process.crawl(PostSpider)
    process.start()

    logger.info('Scrape complete.')

    if result:
        break
    time.sleep(3)

