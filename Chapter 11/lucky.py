#!/usr/bin/env python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4
from googlesearch import search

print('Googling...') #display text while downloading the Google page
res=search(' '.join(sys.argv[1:]))
i=0
for url in res:
    webbrowser.open(url)
    i+=1
    if i==5:break 


