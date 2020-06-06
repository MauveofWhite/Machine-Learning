# @source: Siraj Raval

### Classify a person's sex based on height, weight, and shoe size. ###

from sklearn import tree
from textblob import TextBlob

# Decision tree: Classify sex
# [height, weight, shoe size]
print("######################## Decision Tree Demo ########################")
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65,40]\
, [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], \
[181, 85, 43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', \
'male', 'female', 'male']

# classifier
clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

# result
prediction = clf.predict([[190, 70, 43]])

print(prediction)

print("######################## Sentiment Demo ########################")

wiki = TextBlob("Siraj is angry that he never gets good matches on Tinder")

print("Tags are: ", wiki.tags)
print("Words are: ", wiki.words)
print("Polarity: [-1, 1]. -1 is sadest, 1 is happiest.")
print("The polarity is: ", wiki.sentiment.polarity)
