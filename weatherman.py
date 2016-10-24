from sklearn import tree
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import linear_model

import json

import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

import numpy

import learn

training_filename = './flatteneddata/2000-2010.json'
test_filename = './flatteneddata/2011.json'
numIterations = 100

classifier = tree.DecisionTreeClassifier()

with open(training_filename) as data_file:
    trainings = json.load(data_file)
with open(test_filename) as data_file:
    tests = json.load(data_file)

def getScore(expected, actual):
    numCorrect = 0
    length = len(expected)
    for index in range(0, length):
        if(expected[index] == actual[index]):
            numCorrect += 1
    return numCorrect

expected = map(learn.getClassification, tests)
actual = learn.predict(classifier, trainings, tests)

def testAlgo(name, classifier, iterations, output=None):
    print name
    expected = map(learn.getClassification, tests)
    testCount = len(expected)
    scores = []
    for iteration in range(0, iterations):
        actual = learn.predict(classifier, trainings, tests)
        scores.append(getScore(expected, actual))
    # print scores
    average = numpy.mean(scores)
    percentage = int((float(average) / float(testCount)) * 100.0)
    # print str(average) + "/" + str(float(totalCount)) + "\n"
    print str(percentage) + '%'

testAlgo(
    "Decision Tree",
    tree.DecisionTreeClassifier(),
    numIterations
)
testAlgo(
    "Nearest Neighbors",
    KNeighborsClassifier(n_neighbors=5, weights='distance'),
    numIterations
)
testAlgo(
    "Gaussian Naive Bayes",
    GaussianNB(),
    numIterations
)
# testAlgo(
#     "SVN",
#     svm.SVC(),
#     numIterations
# )
testAlgo(
    "Stochastic Gradient Descent",
    SGDClassifier(loss="hinge", penalty="l2"),
    numIterations
)
# testAlgo(
#     "Linear Regression",
#     linear_model.LinearRegression(),
#     numIterations
# )
