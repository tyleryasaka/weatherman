def getFeatures(sample):
    return sample['features']

def getClassification(sample):
    return sample['classification']

def predict(classifier, trainings, tests):
    data = map(getFeatures, trainings)
    target = map(getClassification, trainings)
    testData = map(getFeatures, tests)
    fit = classifier.fit(data, target)
    return fit.predict(testData)
