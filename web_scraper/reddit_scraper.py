```python
import scrapy
from scrapy.crawler import CrawlerProcess
from web_scraper.spiders.reddit_spider import RedditSpider
from web_scraper.pipelines import JsonWriterPipeline
from web_scraper.items import RedditScraperItem
from web_scraper import settings

class RedditScraper:
    def __init__(self):
        self.process = CrawlerProcess(settings={
            'BOT_NAME': 'reddit_scraper',
            'SPIDER_MODULES': ['web_scraper.spiders'],
            'NEWSPIDER_MODULE': 'web_scraper.spiders',
            'ROBOTSTXT_OBEY': True,
            'ITEM_PIPELINES': {'web_scraper.pipelines.JsonWriterPipeline': 1},
            'FEED_FORMAT': 'json',
            'FEED_URI': 'output.json'
        })

    def run_spider(self, spider):
        self.process.crawl(spider)
        self.process.start()

if __name__ == "__main__":
    scraper = RedditScraper()
    scraper.run_spider(RedditSpider)
```