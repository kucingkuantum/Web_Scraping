# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:18:38 2019

@author: syahr
"""

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd
import lxml.html as lh


def scrap_table(url):
#    url = 'https://ipho-unofficial.org/countries/'
    page = requests.get(url)

    
    #Store the contents of the website under doc
    doc = lh.fromstring(page.content)
    #Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')
    
    #Create empty list
    col=[]
    i=0
    #For each row, store each first element (header) and an empty list
    for t in tr_elements[0]:
        i+=1
        name=t.text_content()
    #    print ('%d:"%s"'%(i,name))
        col.append((name,[]))
        
    
    for j in range(1,len(tr_elements)):
        #T is our j'th row
        T=tr_elements[j]
        
    
        i=0
        
        #Iterate through each element of the row
        for t in T.iterchildren():
            data=t.text_content() 
            #Check if row is empty
            if i>0:
            #Convert any numerical value to integers
                try:
                    data=int(data)
                except:
                    pass
            #Append the data to the empty list of the i'th column
            col[i][1].append(data)
            #Increment i for the next column
            i+=1
        
    Dict={title:column for (title,column) in col}
    df=pd.DataFrame(Dict)
    return df


def medals_all(urlc):
#    urlc = url + test_country

    req = requests.get(urlc)
    soup = BeautifulSoup(req.content, 'html5lib')

    dl_data = soup.find_all("dd")
    for dlitem in dl_data:
        dlitem.string
    
    medals = (dlitem.string).split()
    gold, silver, bronze, hm = float(medals[2]),float(medals[5]),float(medals[8]),float(medals[11])
    return gold, silver, bronze, hm
