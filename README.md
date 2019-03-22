## Topic Modeling In Event Driven Stock Price Prediction

### 1. Gathering posts from financial news and stock market related subreddits
Using crontab job `*/5 * * * * cd /Users/selenacardona/redditcrawler && python2 app.py >> /Users/selenacardona/redditcrawler/python_output2.log` to scrape subreddit posts in 5 minute intervals and feed to MongoDB database.

Screenshot of MongoDB Compass UI to keep track of each post retrieved.
![alt text](https://raw.githubusercontent.com/cardosel/Topic-Modeling-In-Event-Driven-Stock-Price-Prediction/master/mongodb_compass.jpg)
