import numpy as np
import pandas as pd

encFile = open('RBFiles/itemtext.rb', "r", encoding='utf8')
allLines = encFile.readlines()

allCodes = [] #uppercase code
allNames = [] #actual string name
allDesc = [] #description

for line in allLines:
    if(len(line) == 0):
        continue
    if(line[0] == ':'):
        endLoc = line.find('=')
        allCodes.append(line[1:endLoc-1])
    elif(line.find(':desc') != -1):
        line = line.replace('\n', '')
        startLoc = line.find('>')
        allDesc.append(line[startLoc+3:-2])
    elif(line.find(':name') != -1):
        line = line.replace('\n', '')
        startLoc = line.find('>')
        allNames.append(line[startLoc+3:-2])

combinedList = list(zip(allCodes, allNames, allDesc))

newDatabase = pd.DataFrame(combinedList, columns=['CodeName', 'Name', 'Description'])

print(newDatabase)

newDatabase.to_csv('RBFiles/itemNames.csv')
