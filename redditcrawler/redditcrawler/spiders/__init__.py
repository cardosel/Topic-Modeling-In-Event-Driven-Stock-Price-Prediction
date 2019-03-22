# This package will contain the spiders of this Scrapy project

import os
from datetime import datetime as dt
import scrapy
from redditcrawler.items import RedditItem

def get_subs_to_scrape(item):
    # pulls list of subreddits to scrape from text file
    
    subreddits = []
        
    filepath = '/Users/selenacordona/redditcrawler/redditcrawler/spiders/subreddits.txt'
        
        # open file and parse crawler
    with open(filepath, 'r') as f:
        for line in f.readlines():
            subreddits.append((line.strip('\n')))
    return subreddits



class PostSpider(scrapy.Spider):
    name = 'post'
    allowed_domains = ['reddit.com']
        
    reddit_urls = [
        'wallstreetbets',
        'stocks',
        'stock_picks',
        'stockmarket'
    ]
        
    start_urls = ['https://old.reddit.com/r/' + sub + '/new/' \
        for sub in reddit_urls]
    
    def parse(self, response):
        # get the subreddit from the url
        subreddit = response.url.split('/')[4]
        
        #parse through each post
        for post in response.css('div.thing'):
            item = RedditItem()
                
            item['date'] = dt.today()
            item['date_str'] = item['date'].strftime('%Y-%m-%d')
            item['subreddit'] = subreddit
            item['title'] = post.css('a.title::text').extract_first()
            
            item['url'] = post.css('a.title::attr(href)').extract_first()
            ## if self-post, add reddit base url (as it's relative by default)
            if item['url'][:3] == '/r/':
                item['url'] = 'https://old.reddit.com' + item['url']
    
            item['score'] = post.css('div.unvoted::text').extract_first()
            try:
                int(item['score'])
            except:
                continue
            item['commentsUrl'] = post.css('a.comments::attr(href)').extract_first()
            item['linkFlair'] = post.css('span.linkflairlabel::text').extract_first()
            
            yield item