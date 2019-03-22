# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RedditItem(scrapy.Item):

# Defining containers for the data we will scrape

    date = scrapy.Field()
    date_str = scrapy.Field()
    subreddit = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
    commentsUrl = scrapy.Field()
    linkFlair = scrapy.Field()
