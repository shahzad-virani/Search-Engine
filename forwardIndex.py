import json
from bs4 import BeautifulSoup
import urllib.request as URL
import re

def urlOpener(url):
    print('The url is {}'.format(url))
    try:
        res=URL.urlopen(url).read().decode()
        html=BeautifulSoup(res,'html.parser')
        for x in html.findAll('script'):
            html.script.decompose()
        for x in html.findAll('link'):
            html.link.decompose()
        try:
            html.find('div', id="mw-panel").decompose()
        except:
            pass
        try:
            html.find('div', id="mw-head").decompose()
        except:
            pass
        try:
            html.find('div', id="footer").decompose()
        except:
            pass
        try:
            html.find('div',{'class':'reflist'}).decompose()
        except:
            pass
        return html.get_text()
    except:
        print('error during opening')
        return False


def createIndex(url,html,dic):
        splitted=html.split()
        for word in splitted:
            if dic[url].get(word) is None:
                dic[url].update({word:1})
            else:
                dic[url][word]=dic[url].get(word)+1


def main():
    file=open('url3.json','r')
    urls=json.load(file)
    indexFile=open('forwardindex.json','w',encoding='utf-8')
    d=dict()
    for k in urls:
        html=urlOpener(urls[k])
        if html is False:continue
        d[urls[k]]=dict()
        createIndex(urls[k],html,d)
        json.dump(d,indexFile)


if __name__=="__main__":main()
