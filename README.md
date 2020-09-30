# Tweet Sentiment Analysis

This is a course project that analyzed the sentiment of tweets posted in 2016 U.S. Election Day. (Indian tweets were wayyyy too hard)

We try to figure out whether using the social media can help predict the election result.

### Resulting Accuracy

The accuracy varies because we randomly split our training sets. But it should be stable at around $[65, 75]$. This is a demo run:

- Original Naive Bayes: 72.9607250755287
- Sklearn Multinomial Naive Bayes: 70.2416918429003
- Sklearn Bernoulli Naive Bayes: 72.35649546827794
- Sklearn Logistic Regression: 70.69486404833837
- Sklearn Linear SVC: 67.97583081570997
- Sklearn SGD classifier: 67.06948640483384
