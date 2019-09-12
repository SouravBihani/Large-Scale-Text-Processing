from bs4 import BeautifulSoup
import requests


def ScrapData(inputFileName):
    i=1
    text =""
    #textFile = open(outputFileName,"wb")
    with open(inputFileName, "r") as f:
        suffix =inputFileName.split(".")[0]
        try:

            for htmlLink in f:
                print(htmlLink)
                page =requests.get(htmlLink.split("  ")[1])
                data = page.text
                soup = BeautifulSoup(data, 'html.parser')
                for article in soup.find_all('article'):
                    for para in article.find_all('p'):
                        text += para.get_text().encode('utf-8')
                if text != "":
                    textFile = open("/Users/dev/PycharmProjects/DIC/NYTimes/Scraped/"+str(i) + "_" + suffix +".txt","wb")
                    textFile.write(text)
                    i= i+1
                    text =""
        except:
            textFile.close()
if __name__ == '__main__':
    ScrapData(inputFileName="nba.txt")
