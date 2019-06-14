import urllib.request as URL
from bs4 import BeautifulSoup
import json

def retrieve(reqUrl,urls,file1,ind):
    try:
        response=URL.urlopen(reqUrl).read().decode('utf-8')
        html=BeautifulSoup(response,'html.parser')
        for url in html.findAll('a'):
            if urls.get('url.get(title)') is None:
                urls[url.get('title')]="https://en.wikipedia.org"+str(url.get('href'))
        if ind%5==0:
            file1.seek(0)
            print(json.dumps(urls,indent=4),file=file1)
        for i in urls.values():
            print("{}th is made".format(ind))
            ind=ind+1
            retrieve(i,urls,file1,ind)
    except:
        print("error is raised")
        retrieve(reqUrl,urls,file1,ind)


def main():
    initialUrl="https://en.wikipedia.org/wiki/Main_Page"
    urls=dict()
    index=0
    file1=open('url1.json','w')
    retrieve(initialUrl,urls,file1,index);


if __name__=="__main__":
    main()
