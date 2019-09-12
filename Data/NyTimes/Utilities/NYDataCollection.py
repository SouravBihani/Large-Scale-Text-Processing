import csv
import time
import json
import requests


def RetreiveData(acessKey, noOfPages, queryString, outputFile):


    count = 0
    counter = 0
    for count in range(0,noOfPages):
        url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key='+acessKey+'&q=' +queryString +'&begin_date=20190101&end_date=20190325&fl=lead_paragraph%2Cabstract%2Cheadline%2Csnippet%2Cweb_url&page='+str(count)
        print (" Count : ",count," attempting :",url)
        dataurl = requests.get(url,[])
        jsonData = dataurl.json()
        for dest in jsonData['response']['docs']:
            if dest == None:
                break
            f = open(outputFile,"a")
            html =dest['web_url']
            counter = counter +1
            f.write(str(counter) + "  " + html + "\n")
            f.close()
        dataurl.close()
        count+=1
        time.sleep(10)

if __name__ == '__main__':
    RetreiveData('Dl3uPyjAvNgWZ7GetBN90Go3n0ud71oU',50,"fcbarcelona","fcb.txt")