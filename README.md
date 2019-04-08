## Topic Modeling In Event Driven Stock Price Prediction

### 1. Gathering posts from financial news and stock market related subreddits
Using crontab job `*/5 * * * * cd /Users/selenacardona/redditcrawler && python2 app.py >> /Users/selenacardona/redditcrawler/python_output2.log` to scrape subreddit posts in 5 minute intervals and feed to MongoDB database.

Screenshot of MongoDB Compass UI to keep track of each post retrieved.
![alt text](https://raw.githubusercontent.com/cardosel/Topic-Modeling-In-Event-Driven-Stock-Price-Prediction/master/mongodb_compass.jpg)

### 2. Comparison between LDA model on a Bag of Words Dataset and LDA TF-IDF Model on comments.
```
unseen_document = "Apple"
bow_vector = dictionary.doc2bow(tokenization(unseen_document))
for index, score in sorted(lda_model_tfidf[bow_vector], key=lambda tup: -1*tup[1]):
    print("Score: {}\t Topic: {}".format(score, lda_model_tfidf.print_topic(index, 5)))
    
Score: 0.549983978271	 Topic: 0.045*"invest" + 0.030*"appl" + 0.024*"thing" + 0.016*"need" + 0.015*"like"
Score: 0.0500056371093	 Topic: 0.027*"think" + 0.026*"like" + 0.022*"peopl" + 0.015*"go" + 0.014*"card"
Score: 0.0500030145049	 Topic: 0.051*"compani" + 0.025*"know" + 0.024*"stock" + 0.018*"peopl" + 0.015*"think"
Score: 0.0500019192696	 Topic: 0.032*"market" + 0.032*"stock" + 0.025*"long" + 0.024*"sell" + 0.019*"week"
Score: 0.0500012598932	 Topic: 0.036*"like" + 0.032*"money" + 0.015*"month" + 0.014*"need" + 0.013*"market"
Score: 0.0500011965632	 Topic: 0.029*"year" + 0.028*"term" + 0.023*"long" + 0.019*"price" + 0.019*"call"
Score: 0.0500009134412	 Topic: 0.025*"fuck" + 0.018*"like" + 0.018*"market" + 0.016*"think" + 0.016*"year"
Score: 0.050000756979	 Topic: 0.052*"time" + 0.027*"strong" + 0.022*"year" + 0.013*"like" + 0.013*"close"
Score: 0.0500007234514	 Topic: 0.029*"money" + 0.028*"short" + 0.027*"http" + 0.027*"like" + 0.024*"href"
Score: 0.050000615418	 Topic: 0.054*"trade" + 0.041*"good" + 0.024*"bond" + 0.022*"market" + 0.021*"stock"```

### 3. Performance evaluation between Bigrams Model and LDA TF-IDF Model on comments.
