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
Score: 0.050000615418	 Topic: 0.054*"trade" + 0.041*"good" + 0.024*"bond" + 0.022*"market" + 0.021*"stock"
```

### 3. Performance evaluation between Bigrams Model and LDA TF-IDF Model on comments.
#### Example: Extracting Trigrams from "Uber" Mentions
```
data = pd.read_csv("training-data-2019-04-11.csv")
sell_data = data[data.comments.str.contains("Uber")]
data = sell_data
data_text = data[['comments']]
data_text= data_text.drop_duplicates(subset='comments', keep="last").reset_index()
data_text['index'] = data_text.index
documents = data_text
processed_documents = documents['comments'].map(tokenization)
sentences = processed_documents
bigrams = Phrases(sentences, min_count=2, threshold=100)
trigrams = Phrases(bigrams[sentences], threshold=100)
sorted(trigrams.vocab.items(), key=lambda x:x[1], reverse=True)[110:170]
[('travel', 12),
 ('player', 12),
 ('data', 12),
 ('busi_model', 12),
 ('like_lyft', 12),
 ('month', 12),
 ('soon', 12),
 ('manufactur', 12),
 ('stop', 12),
 ('lose_money', 12),
 ('pinterest', 12),
 ('uber_go', 12),
 ('app', 12),
 ('instead', 12),
 ('hold', 11),
 ('offer', 11),
 ('uber_market', 11),
 ('number', 11),
 ('sell', 11),
 ('person', 11),
 ('us', 11),
 ('tri', 11),
 ('expand', 11),
 ('away', 11),
 ('product', 11),
 ('drop', 11),
 ('space', 11),
 ('gonna', 11),
 ('self_drive_car', 11),
 ('interest', 11),
 ('nofollow', 11),
 ('scale', 11),
 ('beat', 11),
 ('hail', 11),
 ('brand', 11),
 ('risk', 11),
 ('insur', 11),
 ('capit', 11),
 ('rent', 11),
 ('rideshar', 11),
 ('option', 11),
 ('overvalu', 10),
 ('think_uber', 10),
 ('regul', 10),
 ('take', 10),
 ('industri', 10),
 ('plan', 10),
 ('worth', 10),
 ('rais', 10),
 ('global', 10),
 ('yeah', 10),
 ('area', 10),
 ('put', 10),
 ('save', 10),
 ('ford', 10),
 ('margin', 10),
 ('file', 10),
 ('wouldn', 10),
 ('bought', 10),
 ('second', 9)]
 ```

### 4. Create Document Feature Matrix from N-Grams Model after applying LDA for dimensionality reduction as input to            CNN.




Supporting Sources:
Topic Modeling based Sentiment Analysis on Social Media
for Stock Market Prediction: https://www.aclweb.org/anthology/P15-1131

Stock Market Prediction with Deep Learning: A Character-based Neural Language Model for Event-based Trading:
https://aclweb.org/anthology/U17-1001

Sentiment analysis of Twitter data for predicting stock market movements
https://ieeexplore.ieee.org/document/7955659
