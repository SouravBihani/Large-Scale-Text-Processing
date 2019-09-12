import bs4
import requests
import json
from  io import  StringIO
import gzip
import csv
import codecs
from bs4 import BeautifulSoup
import sys
import io
import  StringIO
reload(sys)
sys.setdefaultencoding('utf-8')

linker = []
myTopics = ["football","basketball","nba","mls","nfl","nhl","cricket","soccer"]
def GetRecords():
    recordList = []
    ccUrl = "http://index.commoncrawl.org/CC-MAIN-2019-13-index?url=https://www.espn.com/&matchType=domain&output=json"
    response = requests.get(ccUrl)
    if response.status_code ==200:
        records = response.content.splitlines()
        for record in records:
            recordList.append(json.loads(record))
    return recordList


def GetData(recordList):
    count=0
    for record in recordList:
        if count >800:
            break;
        offset, length = int(record['offset']), int(record['length'])
        offset_end = offset + length -1
        prefix = "https://commoncrawl.s3.amazonaws.com/"
        response = requests.get(prefix + record['filename'], headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})
        raw_data = StringIO.StringIO(response.content)
        f = gzip.GzipFile(fileobj=raw_data)
        data = f.read()
        response = ""
        if(len(data)):
            warc,header,response = data.strip().split('\r\n',2)
            parser = BeautifulSoup(response, 'html.parser')
            links = parser.find_all("a")
            if links:
                for link in links:
                    if isinstance(link, str):
                        continue
                    href = link.attrs.get("href")
                    if href is not None:
                        if href.encode('utf-8') not in linker and href.startswith("http"):
                            linker.append(href.encode('utf-8'))
                            count = count +1
                            print(str(count))
                            if count > 800:
                                break

    with open("hrefs_espn19.txt", 'w+') as file:
        for link in linker:
            file.write(link.encode("utf-8"))
            file.write("\n")


    return response

def ScrapData(filename):
    with open(filename) as f:
        try:
            i = 0
            urls = f.read().split()
            for htmlLink in urls:
                print(htmlLink)
                page = requests.get(htmlLink)
                soup = BeautifulSoup(page.text, 'html.parser')
                text = ""
                for para in soup.find_all('p'):
                    text += para.get_text()
                if text != "":
                    text = text.lower()
                    textFile = open(str(i) + "_espn19.txt", "w+")
                    textFile.write(text.encode('utf-8'))
                    i = i + 1
        except:
            print("Something went wrong...")
            textFile.close()


if __name__ == '__main__':
    # Reference -https://www.bellingcat.com/resources/2015/08/13/using-python-to-mine-common-crawl/
    #recordList =GetRecords()
    #GetData(recordList)
    ScrapData("hrefs_espn19.txt")