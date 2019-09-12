
import glob

outputFile = open("/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Common Crawl/MergedCCData.txt","w+")
path = '/Users/aman/PycharmProjects/DIC/BigDataAnalysis/Data/Common Crawl/*.txt'
files = glob.glob(path)
for name in files:
    try:
        with open(name) as f:
            outputFile.write(f.read())
    except:
        print ("Something went wrong")
