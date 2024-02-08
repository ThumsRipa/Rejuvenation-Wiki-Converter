import numpy as np
import pandas as pd

trainerFile = open('RBFiles/ttypetext.rb', "r", encoding='utf8')
trainerLines = trainerFile.readlines()

trainerCode = []
trainerTitle = []
trainerImage = []
trainerMoney = []

curTrainerMoneyFound = False

for line in trainerLines:
    if(len(line) == 0):
        continue
    line = line.replace('\n', '')
    line = line.replace('\t', '')
    if(line.find('},') != -1):
        if(not curTrainerMoneyFound):
           trainerMoney.append(30)
        curTrainerMoneyFound = False
        continue
    if(line.find('=> {') != -1):
        endPos = line.find('=')
        codeName = line[1:endPos-1]
        trainerCode.append(codeName)
        codeName = codeName.split('_')
        fullCodeName = ''
        for splitName in codeName:
            fullCodeName += splitName.capitalize()
        trainerImage.append(fullCodeName+'_TS.png')
        continue
    if(line.find('title') != -1):
        startPos = line.find('>')
        trainerTitle.append(line[startPos+3:-2])
        continue
    if(line.find('moneymult') != -1):
        curTrainerMoneyFound = True
        startPos = line.find('>')
        trainerMoney.append(line[startPos+2:-1])
        continue

combinedList = list(zip(trainerCode, trainerTitle, trainerImage, trainerMoney))

newDatabase = pd.DataFrame(combinedList, columns=['Code', 'Title', 'Image', 'Money'])

print(newDatabase)

newDatabase.to_csv('RBFiles/trainerTypes.csv')