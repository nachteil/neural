import csv

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import *

from math import pow as power

import time
import datetime

workclass = {"Private": 1, "Self-emp-not-inc": 2, "Self-emp-inc": 3, "Federal-gov": 4, "Local-gov": 5, "State-gov": 6,
             "Without-pay": 7, "Never-worked": 8}
education = {"Bachelors": 0, "Some-college": 1, "11th": 2, "HS-grad": 3, "Prof-school": 4, "Assoc-acdm": 5,
             "Assoc-voc": 6, "9th": 7, "7th-8th": 8, "12th": 9, "Masters": 10, "1st-4th": 11, "10th": 12,
             "Doctorate": 13, "5th-6th": 14, "Preschool": 15}
occupation = {"Tech-support": 0, "Craft-repair": 1, "Other-service": 2, "Sales": 3, "Exec-managerial": 4,
              "Prof-specialty": 5, "Handlers-cleaners": 6, "Machine-op-inspct": 7, "Adm-clerical": 8,
              "Farming-fishing": 9, "Transport-moving": 10, "Priv-house-serv": 11, "Protective-serv": 12,
              "Armed-Forces": 13}
sex = {"Male": 1, "Female": 0}
country = {"United-States": 0, "Cambodia": 1, "England": 2, "Puerto-Rico": 3, "Canada": 4, "Germany": 5,
           "Outlying-US(Guam-USVI-etc)": 6, "India": 7, "Japan": 8, "Greece": 9, "South": 10, "China": 11, "Cuba": 12,
           "Iran": 13, "Honduras": 14, "Philippines": 15, "Italy": 16, "Poland": 17, "Jamaica": 18, "Vietnam": 19,
           "Mexico": 20, "Portugal": 21, "Ireland": 22, "France": 23, "Dominican-Republic": 24, "Laos": 25,
           "Ecuador": 26, "Taiwan": 27, "Haiti": 28, "Columbia": 29, "Hungary": 30, "Guatemala": 31, "Nicaragua": 32,
           "Scotland": 33, "Thailand": 34, "Yugoslavia": 35, "El-Salvador": 36, "Trinadad&Tobago": 37, "Peru": 38,
           "Hong": 39, "Holand-Netherlands": 40}

income = {"<=50K": 0, ">50K": 1}

AGE = 0
WORK_CLASS = 1
FINAL_WEIGHT = 2
EDUCATION = 3
EDUCATION_NUM = 4
MARITAL_STATUS = 5
OCCUPATION = 6
RELATIONSHIP = 7
RACE = 8
SEX = 9
GAIN = 10
LOSS = 11
HOURS_PER_WEEK = 12
NATIVE = 13

RESULT = 14


def createInputEntry(row):
    dataRow = (int(row[AGE]),
               workclass[row[WORK_CLASS]],
               education[row[EDUCATION]],
               int(row[EDUCATION_NUM]),
               occupation[row[OCCUPATION]],
               sex[row[SEX]],
               int(row[HOURS_PER_WEEK]))

    expectedResult = income[row[RESULT]]
    return dataRow, expectedResult


def createDataSet(fileName, limit):
    data = []
    rowCount = 0
    with open(fileName, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if '?' not in row:
                try:
                    entry = createInputEntry(row)
                    data.append(entry)
                    rowCount += 1
                except:
                    pass
            if 0 < limit <= rowCount:
                break
    return data

def createNetwork():
    return buildNetwork(7, 30, 1, bias=True, hiddenclass=SigmoidLayer)

def trainNetwork(net, dataSet, epochs):

    ds = SupervisedDataSet(7, 1)
    for entry in dataSet:
        ds.addSample(entry[0], entry[1])

    trainer = BackpropTrainer(net, ds, learningrate=0.10, momentum=0.7)

    startTime = time.time()
    trainer.trainEpochs(epochs=1)
    endTime = time.time()

    epochTime = endTime - startTime
    print "Training netowrk with {0} training entries".format(len(dataSet))
    print "Single epoch training time: {:10.3f}".format(epochTime)
    estimatedSeconds = int(epochTime * epochs)
    print "Estimated training time for {0} epochs: {1} seconds".format(str(epochs), estimatedSeconds)
    print "Starting training at {0}...".format(time.strftime("%H:%M"))

    startTime = time.time()
    trainer.trainEpochs(epochs=epochs)
    endTime = time.time()
    print "Finished {0} epochs training in {1} seconds".format(epochs, endTime - startTime)
    print ""

def getMSE(net, testData):
    errorSum = 0
    for entry in testData:
        data = entry[0]
        expectedResult = entry[1]
        result = net.activate(data)
        errorSum += power(expectedResult - result, 2)
    return errorSum / len(testData)


def verifyBehavior(net, netState, testData):

    print "Executing test for {0} netowrk on {1} test entries...".format(netState, len(testData))

    MSE = getMSE(net, testData)
    print "Mean squared error from {0} tries: {1:5.5f}".format(len(testData), MSE)
    print ""

def getDeviation(arr):

    if len(arr) < 1:
        return 0
    avg = sum(arr) / len(arr)
    s = 0
    for e in arr[:-1]:
        s += power(e-avg, 2)
    return s / len(arr)

def doExperiment(net, trainingData, testData, epochs):

    errors = []

    ds = SupervisedDataSet(7, 1)
    for entry in trainingData:
        ds.addSample(entry[0], entry[1])

    trainer = BackpropTrainer(net, ds, learningrate=0.10, momentum=0.3)

    for e in range(0, epochs+1):
        error = getMSE(net, testData)
        errors.append(error)
        deviation = getDeviation(errors)
        print "{0},{1},{2}".format(e,error,deviation)
        trainer.trainEpochs(epochs=1)

def main():

    trainingData = createDataSet("adult.data", 2000)
    testData = createDataSet("adult.test", 200)

    net = createNetwork()

    startTime = time.time()
    doExperiment(net, trainingData, testData, 200)
    endTime = time.time()
    print "Took: {0}".format(endTime-startTime)

main()





