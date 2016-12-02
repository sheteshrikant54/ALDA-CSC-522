from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB

from sklearn.feature_extraction.text import TfidfVectorizer
from statsmodels.genmod.families.links import sqrt

train = pd.read_csv("D:/MS/ALDA CSC 522/Project/training.csv", header=0, delimiter=",", quoting=3)
print(train.shape)

print(train.columns.values)

num_reviews = train["ImpWords"].size

clean_train_reviews = []

# Loop over each page; create an index i that goes from 0 to the length
# of the words
for i in range( 0, num_reviews):
    clean_train_reviews.append(train["ImpWords"][i])



vectorizer = TfidfVectorizer(max_features=3000,use_idf=False,max_df=0.9,min_df=0.1)

train_data_features = vectorizer.fit_transform(clean_train_reviews)

train_data_features = train_data_features.toarray()

print(train_data_features.shape)

# Sum up the counts of each vocabulary word
dist = np.sum(train_data_features, axis=0)

# For each, print the vocabulary word and the number of times it
# appears in the training set
vocab = vectorizer.get_feature_names()
# print(vocab)
for tag, count in zip(vocab, dist):
    print(count, tag)


# naive = RandomForestClassifier(n_estimators = 100)

naive = MultinomialNB().fit(train_data_features,train["category"])

test = pd.read_csv("D:/MS/ALDA CSC 522/Project/test.csv", header=0, delimiter=",", quoting=3 )
num_reviews = test["ImpWords"].size
clean_test_reviews = []

for i in range( 0, num_reviews):
    clean_test_reviews.append(test["ImpWords"][i])

test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray()

result = naive.predict(test_data_features)

output = pd.DataFrame( data={"Original classification":test["category"], "Prediction":result} )

# Use pandas to write the comma-separated output file
output.to_csv( "D:/MS/ALDA CSC 522/Project/NBPrediction.csv", index=False, quoting=3 )