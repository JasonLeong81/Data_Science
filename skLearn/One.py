import json
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import random

class Sentiment: # Enum
    NEGATIVE = 'NEGATIVE'
    NEUTRAL = 'NEUTRAL'
    POSITIVE = 'POSITIVE'
class Review:
    def __init__(self,text,score):
        self.text = text
        self.score = score
        self.sentiment = self.get_sentiment()
    def get_sentiment(self):
        if self.score <= 2:
            return Sentiment.NEGATIVE
        elif self.score == 3:
            return Sentiment.NEUTRAL
        else:
            return Sentiment.POSITIVE
class ReviewContainer:
    def __init__(self,reviews):
        self.reviews = reviews
    def evenly_distribute(self):
        negative = list(filter(lambda x: x.sentiment == Sentiment.NEGATIVE,self.reviews))
        positive = list(filter(lambda x: x.sentiment == Sentiment.POSITIVE,self.reviews))
        positive_shrunk = positive[:len(negative)]
        self.reviews = negative + positive_shrunk
        random.shuffle(self.reviews)
        # print(len(negative),negative[0].text)
        # print(len(positive),positive[0].text)
    def get_text(self):
        return [x.text for x in self.reviews]
    def get_sentiment(self):
        return [x.sentiment for x in self.reviews]

file_name = 'small.json'
# file_name = 'tt.json'
reviews = []
with open(file_name,'r') as f:
    for i in f:
        review = json.loads(i)
        # print(review['reviewText']) # we will get an error because that's just raw text so we need to use the json module
        # print(review['overall'])
        reviews.append(Review(review['reviewText'],review['overall']))
# print(reviews)
# print(len(reviews))
# print(reviews[0].sentiment)

# BOW (bag of words) #####################################
# this book is great -> [1,1,1,1,0,0,0]
# this book was so bad -> [1,1,0,0,1,1,1]
# histograms of keywords
# TF-IDF -> put more value on important words which BOW cannot due to  1 1

# Prepping Data #######################################
training, test = train_test_split(reviews, test_size=0.33, random_state=42) # When the Random_state is not defined in the code for every run train data will change and accuracy might change for every run. When the Random_state = " constant integer" is defined then train data will be constant For every run so that it will make easy to debug.
# print(len(training),len(test))

training_container = ReviewContainer(training)
test_container = ReviewContainer(test)

training_container.evenly_distribute()
test_container.evenly_distribute()

train_x = training_container.get_text() # 'sss','sss','sss',...
train_y = training_container.get_sentiment() # positive,negative,neutral,...

# print(train_y)
# print(train_x)

test_x = test_container.get_text()
test_y = test_container.get_sentiment()

# print(train_y.count(Sentiment.POSITIVE))
# print(train_y.count(Sentiment.NEGATIVE))


vectorizer = CountVectorizer()

###### TF-IDF (KG) #################################################
# vectorizer = TfidfVectorizer()
train_x_vectors = vectorizer.fit_transform(train_x) # two in one function
test_x_vectors = vectorizer.transform(test_x)
# print(train_x[0])
# print(train_x_vectors[0]) # giving us the unique values' position
# print(train_x_vectors[0].toarray())


import sys
sys.exit()





### Linear SVM
from sklearn import svm
clf_svm = svm.SVC(kernel='linear')
clf_svm.fit(train_x_vectors,train_y)
# print(test_x[0])
# print(test_x_vectors[0])
# print(clf_svm.predict(test_x_vectors[0]))

### Decision Tree
from sklearn.tree import DecisionTreeClassifier
clf_dec = DecisionTreeClassifier()
clf_dec.fit(train_x_vectors, train_y)
# print(clf_dec.predict(test_x_vectors[0]))

### Naive Bayes
from sklearn.naive_bayes import GaussianNB
clf_gnb = DecisionTreeClassifier()
clf_gnb.fit(train_x_vectors, train_y)
# print(clf_gnb.predict(test_x_vectors[0]))


### Logistic regression
from sklearn.linear_model import LogisticRegression
clf_log = LogisticRegression()
clf_log.fit(train_x_vectors, train_y)
# print(clf_log.predict(test_x_vectors[0]))

####### Evaluation
# print(clf_svm.score(test_x_vectors, test_y))
# print(clf_dec.score(test_x_vectors, test_y))
# print(clf_gnb.score(test_x_vectors, test_y))
# print(clf_log.score(test_x_vectors, test_y))

### F1 scores (higher the better)
from sklearn.metrics import f1_score
# print(f1_score(test_y, clf_svm.predict(test_x_vectors), average=None, labels=[Sentiment.POSITIVE, Sentiment.NEGATIVE]))
# print(f1_score(test_y, clf_log.predict(test_x_vectors), average=None, labels=[Sentiment.POSITIVE, Sentiment.NEUTRAL, Sentiment.NEGATIVE]))

### if all models have the same issues, then there must be some problem with the date rather than the model
test_set = ['very fun', "bad book do not buy", 'horrible waste of time']
new_test = vectorizer.transform(test_set)
# print(clf_svm.predict(new_test)) # try very brilliant
# print(train_y.count(Sentiment.NEGATIVE))

###### TF-IDF (Krish Naik) #################################################
# better than bow due to semantics of keywords
# Term frequency : number of repetition of words in sentence / number of words in sentence
# Inverse Document frequency : log (number of sentences / number of sentences containing words)
# TF*IDF
# output feature ???

###### Tuning our model: Grid Search ######################################
from sklearn.model_selection import GridSearchCV
parameters = {'kernel': ('linear', 'rbf'), 'C': (1,4,8,16,32)}
svc = svm.SVC()
clf = GridSearchCV(svc, parameters, cv=5)
clf.fit(train_x_vectors, train_y)
# print(clf.score(test_x_vectors, test_y))

###### Saving Model ##############################################################
import pickle
with open('./models.pkl','wb') as f:
    pickle.dump(clf,f)
###### Loading saved model ################################################################
with open('./models.pkl','rb') as ff:
    loaded_clf = pickle.load(ff)
print(test_x[0])
print(loaded_clf.predict(test_x_vectors[0]))

###### Perceptron ########################################################
# from sklearn.linear_model import Perceptron
# clf = Perceptron(tol=1e-3, random_state=0)
# clf.fit(X, y)

###### Confusion Matrix ############################################################


###### word2vec (Krish Naik) ###################################################################

