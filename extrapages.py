import json
from bs4 import BeautifulSoup
import urllib.request as URL

error=""" =============================== """


def main():
    out=open('url1.json','r')
    urls=json.load(out)
    out.close()
    new_dict=dict()
    index=1
    for items in urls:
        try:
            res=URL.urlopen(urls[items]).read().decode()
        except:
            print('the requested url has not opened {}'.format(urls[items]),flush=True)
            continue
        html=BeautifulSoup(res,'html.parser')
        see_also=html.find('span',id="See_also")
        if see_also is None:
            continue
        see_also=see_also.parent.next_sibling.next_sibling
        [x.decompose() for x in see_also.findAll('span',class_='mw-editsection')]
        [x.decompose() for x in see_also.findAll('img')]
        print(error)
        for url in see_also.findAll('a'):
            if urls.get('url.get(title)') is None:
                print("https://en.wikipedia.org"+str(url.get('href')))
                new_dict[url.get('title')]="https://en.wikipedia.org"+str(url.get('href'))
        print(error)
        print('{} turn is made'.format(str(index)))
        index=index+1
    out=open('related.json','w')
    json.dump(new_dict,out)
    out.close()
    print(error,error)
    print('everything is done')
    print(error,error)


if __name__ == '__main__':
    main()
