```python
from scrapy import Item, Field

class RedditScraperItem(Item):
    title = Field()
    url = Field()
    author = Field()
    upvotes = Field()
    comments = Field()
```