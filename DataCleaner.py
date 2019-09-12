#!/usr/bin/python

import re
# if there is a problem in downloading nltk data, then run the Install Certificates.command available in your Python folder and then execute the download command
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer
import os



def tokenize(text, regExForDeletingWords):
    ps = PorterStemmer()
    resultTokens = []
    tokens = [t for t in text.split()]
    for token in tokens:
        # match = re.sub(r'([^\s\w]|_)+', '', token)
        # type(match)
        # if match is None:
        if token.isalpha():
            ps.stem(token)
            resultTokens.append(token)
    return resultTokens


def SetupDataClean():
    import nltk
    # if there is a problem in downloading nltk data, then run the Install Certificates.command available in your Python folder and then execute the download command
    nltk.download('stopwords')
    #Reference =https://docs.python.org/3/library/re.html
    deleteString = [ ]
    deleteWordsRegEx = re.compile(r'(' + ',' +'.' + '"' + '|'.join(deleteString) + ')', re.VERBOSE | re.IGNORECASE)
    return deleteWordsRegEx



def Clean(regExForDeletingWords,inputFileName, outputFileName):
    customStopWords = ["get", "account", "also", "last", "first", "new", "make", "may","said","con","made","live","los","like","would","could","might","de","en","el","la","se"]

    textFile = open(outputFileName,"w")
    #with open(inputFileName, "r", encoding='utf-8') as file:
    for filelineno, line in enumerate(open(inputFileName)):
            if len(line) == 0:
                continue;
            line = line.strip()
            line = line.lower();
            punctuationToRemove = list(string.punctuation)
            stop = stopwords.words('english')  + punctuationToRemove + customStopWords
            new_line = [term for term in tokenize(line,regExForDeletingWords) if not term in stop]
            new_line = [word for word in new_line if not len(word) == 1]
            new_line = [word for word in new_line if not len(word) == 2]
            for word in new_line:
                textFile.write(word.lower() + " ")
    textFile.close();


if __name__ == '__main__':

    regEx = SetupDataClean()
    Clean(regEx,"/Users/dev/PycharmProjects/DIC/Twitter/mlbText.txt", "/Users/dev/PycharmProjects/DIC/Cleaned/Twitter/cleanedMlb.txt")
    # Map(regEx,"/Users/dev/PycharmProjects/DIC/Twitter/Aman_data/football.txt", "/Users/dev/PycharmProjects/DIC/Cleaned/Twitter/Cleanedfootball.txt")
    # Map(regEx,"/Users/dev/PycharmProjects/DIC/Twitter/Aman_data/fifa.txt", "/Users/dev/PycharmProjects/DIC/Cleaned/Twitter/Cleanedfifa.txt")
    # Map(regEx,"/Users/dev/PycharmProjects/DIC/Twitter/Aman_data/messi.txt", "/Users/dev/PycharmProjects/DIC/Cleaned/Twitter/Cleanedmessi.txt")
    # # Map(regEx,"/Users/dev/PycharmProjects/DIC/Twitter/messi.txt", "/Users/dev/PycharmProjects/DIC/Cleaned/Twitter/messiCleaned.txt")
    # # Map(regEx,"/Users/dev/PycharmProjects/DIC/Twitter/mlsText.txt", "/Users/dev/PycharmProjects/DIC/Cleaned/Twitter/mlsTextCleaned.txt")
    # # Map(regEx,"/Users/dev/PycharmProjects/DIC/Twitter/nbaText.txt", "/Users/dev/PycharmProjects/DIC/Cleaned/Twitter/nbaTextCleaned.txt")
    # Map(regEx,"/Users/dev/PycharmProjects/DIC/Twitter/nhlText.txt", "/Users/dev/PycharmProjects/DIC/Cleaned/Twitter/nhlTextCleaned.txt")
    # Map(regEx,"/Users/dev/PycharmProjects/DIC/Twitter/realmadrid.txt", "/Users/dev/PycharmProjects/DIC/Cleaned/Twitter/realmadridCleaned.txt")
    # Map(regEx,"/Users/dev/PycharmProjects/DIC/Twitter/ronaldo.txt", "/Users/dev/PycharmProjects/DIC/Cleaned/Twitter/ronaldoCleaned.txt")
    # Map(regEx,"/Users/dev/PycharmProjects/DIC/Twitter/zidane.txt", "/Users/dev/PycharmProjects/DIC/Cleaned/Twitter/zidaneCleaned.txt")

