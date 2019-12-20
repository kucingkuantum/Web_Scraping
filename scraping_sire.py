# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:18:38 2019

@author: syahr
"""
import plotly.graph_objects as go
import requests
import urllib.request
#import time
from bs4 import BeautifulSoup
import pandas as pd
import lxml.html as lh
import scraping_function as sf




url = 'https://ipho-unofficial.org/countries/'
df = sf.scrap_table(url)


medals = []
for i in range(0,5):
    test_country = df['Code'][i]
    urlc = url + test_country
    medals.append(sf.medals_all(urlc))
    print(sf.medals_all(urlc))
    
df.append(medals)

se= pd.DataFrame(medals,columns=['gold','silver','bronze','hm'])
dnew = pd.concat([df,se],axis=1)
dnew.drop(dnew.columns[[2, 3]], axis=1, inplace=True)

fig = go.Figure(data=go.Choropleth(
    locations = dnew['Code'],
    z = dnew['gold'],
    text = df['Country'],
    colorscale = 'Hot',
    autocolorscale=True,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '',
    colorbar_title = 'Gold Medal',
))

fig.update_layout(
    title_text='IPHO Medal',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
#        text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
#            CIA World Factbook</a>',
        showarrow = False
    )]
)

fig.write_image("fig1.png")
fig.show()
