# -*- coding: utf-8 -*-
import random

def getAverage(singleList):
    response = 0
    for element in singleList:
        response += float(element)
    response = response / len(singleList)
    return response

def run():
    singleList = list()
    for i in range(random.randint(0, 100)):
        singleList.append(random.randint(i, 100))

    average = getAverage(singleList)
    print("The average is: {} of the: {}".format(average, singleList))

if __name__ == "__main__":
    run()