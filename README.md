# Opinion-Mining
In this method we have several variations in the training the Naïve Bayes Classifier.

Method I:
In this method of finding sentiment we used the set 5333 and 5332 positive and negative movie reviews provided by Cornell University.
We used three-fourth of the data set for training and one-fourth for testing.

Method II :
In this method we have used same data set but trained the classifier with most frequent 10,000 Features based on their Chi-Square Score
                  Χ^2(t,c) =( N∗(AD−CB)^2) / [(A+C)∗(B+D)∗(A+B)∗(C+D)]
				  
Method III:
In this we trained the classifier with 10000 features extracted from the movie reviews
 and tested on Twitter data collected from      http://inclass.kaggle.com/c/si650winter11/data
 
Method IV:
In this  we trained  and tested with the Twitter data set previously collected. We used  three-fourth for  training and one-fourth for testing purposes.

Method V:
In this we trained classifier using mixed data set of both movie reviews and twitter data set. Nine-tenth of the data set is used for training and one-tenth is used for testing.


Baseline model(approach-II)
  In this method of calculating sentiment of the tweets we used bag of positive and negative words of size 2400+ and 4000+ respectively.
We extracted the opinion features from the tweet text and added +1 if the word is in positive bag of words and -1 if it is negative bag of words.
Special feature: We added positive and negative emoticons as they play a major role in determining sentiment expressed by the people.
 
  

