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
            for word in new_line:
                textFile.write(word + " ")
    textFile.close();

if __name__ == '__main__':

    regEx = SetupDataClean()
    for filename in os.listdir("/Drive/UB/Spring19/DIC/Project2/Lab2/Data/Common Crawl/"):
        if filename.endswith(".txt"):
            print(str(filename))
            Clean(regEx, "/Drive/UB/Spring19/DIC/Project2/Lab2/Data/Common Crawl/" + filename,
                  "/Drive/UB/Spring19/DIC/Project2/Lab2/Data/Common Crawl/CleanedData/" + str(filename).split(".")[
                      0] + "_cleaned.txt")

    #Map(regEx,"/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/footballText.txt", "/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/CleanedFootballData.txt")
    #Clean(regEx,"/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/nbaText.txt", "/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/CleanedNbaData.txt")
    #Clean(regEx,"/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/nhlText.txt", "/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/CleanedNhlData.txt")
    #Clean(regEx, "/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/mlbText.txt","/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Twitter/CleanedData/CleanedMlbData.txt")
