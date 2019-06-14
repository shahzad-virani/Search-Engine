import os
from bs4 import BeautifulSoup
import json

error = " =============================== "


def main():
    print(error);print('forward indexing has started');print(error)
    file1=open('url.json','r')
    res=json.load(file1)
    file1.close()
    file1=open('related.json','r')
    temp=json.load(file1)
    res.update(temp)
    index=dict()
    counter=1
    for filename in os.listdir('html_files'):
        print('{} file'.format(counter))
        counter=counter+1
        response=open('html_files//'+str(filename),'r')
        html=BeautifulSoup(response,'html.parser')
        response.close()
        [x.decompose() for x in html.findAll('span',class_='mw-editsection')]
        if index.get(filename[:-5]) is None:
            index[filename[:-5]]=[res[filename[:-5]],dict()]
        else:
            continue
        for h2 in html.findAll('h2'):
            list_res=h2.get_text().split()
            for word in list_res:
                index[filename[:-5]][1][word]=[list_res.index(word),'h2']
        for p in html.findAll('p'):
            list_res=p.get_text().split()
            for word in list_res:
                index[filename[:-5]][1][word]=[list_res.index(word),'p']
        for h3 in html.findAll('h3'):
            list_res=h3.get_text().split()
            for word in list_res:
                index[filename[:-5]][1][word]=[list_res.index(word),'h3']
    out=open('forwardIndex.json','w')
    json.dump(index,out)
    out.close()



if __name__ == '__main__':
    main()
