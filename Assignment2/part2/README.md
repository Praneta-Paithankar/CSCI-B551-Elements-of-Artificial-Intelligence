Part 2:  Tweet classification
A classic application of Bayes Law is in document classification.  Let’s examine one particular classification problem:  estimating where a Twitter “tweet” was sent, based only on the content of the tweet itself.  

We’ll use a bag-of-words model, which means that we’ll represent a tweet in terms of just an unordered “bag” of words instead of modeling anything about its grammatical structure.  In other words, a tweet can be modeledas simply a histogram over the words of the English language (or, more generally, all possible tokens thatoccur on Twitter). 

If, for example, there are 100,000 words in the English language, then a tweet can be represented as a 100,000-dimensional binary vector, where in each dimension there is a 1 if the word appearsin the tweet and a zero otherwise. 
Of course, vectors will be very sparse (most entries are zero).

Implement a Naive Bayes classifier for this problem.  For a given tweetD,  we’ll need to evaluateP(L=l|w1, w2, ..., wn), the posterior probability that a tweet was taken at one particular location (e.g.,l= Chicago) given  the  words  in  that  tweet.   Make  the  Naive  Bayes  assumption,  which  says  that  for  any i!=j,wi is independent from wj given L.To help you get started, we’ve provided a dataset in your GitHub repo of tweets, labeled with their actualgeographic locations, split into a training set and a testing set.  We’ve restricted to a set of a dozen NorthAmerican cities (Chicago, Philadelphia, etc.), so your task is to classify each tweet into one of twelve different categories. 

Train your model on the training data and measure performance on the testing data in terms ofaccuracy (percentage of documents correctly classified).Your program should accept command line arguments like this:

./geolocate.py training-file testing-file output-file

The  program  should  then  load  in  the  training  file,  estimate  the  needed  probabilities  to  build  a  Bayesianmodel, and apply them to each tweet in the testing file, and then write the results into output-file. 
The file format of the training and testing files is simple:  one tweet per line, with the first word of the line indicatingthe actual location. 

Output-file should have the same format, except that the first word of each line shouldbe your estimated label, the second word should be the actual label, and the rest of the line should be thetweet itself. 
Your program should also output (to the screen) the top 5 words associated with each of the 123
locations (i.e.  the words for whichP(L=l|w) is the highest for eachl)
