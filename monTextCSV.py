import numpy as np
import pandas as pd

encFile = open('RBFiles/montext.rb', "r", encoding='utf8')
allLines = encFile.readlines()

allCodes = [] #uppercase code
allNums = []
allNames = [] #actual string name

for line in allLines:
    if(len(line) == 0):
        continue
    if(line[0] == ':'):
        endLoc = line.find('=')
        allCodes.append(line[1:endLoc-1])
    elif(line.find('dexnum') != -1):
        line = line.replace('\n', '')
        startLoc = line.find('>')
        allNums.append(line[startLoc+2:-1])
    elif(line.find(':name') != -1):
        line = line.replace('\n', '')
        startLoc = line.find('>')
        allNames.append(line[startLoc+3:-2])

combinedList = list(zip(allCodes, allNums, allNames))

newDatabase = pd.DataFrame(combinedList, columns=['CodeName', 'DexNum', 'Name'])

print(newDatabase)

newDatabase.to_csv('RBFiles/pokemonDexNums.csv')
