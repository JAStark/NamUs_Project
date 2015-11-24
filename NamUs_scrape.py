# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:17:15 2015

@author: jenniferstark
"""

'''
This script loops through a range of potential case numbers, looks for them
on the website, and writes them to a .html file on the local machine.
'''

import requests
from bs4 import BeautifulSoup
from time import sleep

# code to create and loop through each potential case number.
# if it finds one, it will call 'get_html' to grab it, and write it to file
def namus_scrape(cases):
    for case in cases:
        try:
            print(case)
            get_html(case)
        except:
            continue
    sleep(2)

# code to create emtpy .html file, grab data for current case number from 
# appropriate URL and write it to currently empty .html file
def get_html(case_id):
    case_html = ('case_' + str(case_id) + '.html') 
    with open((case_html), 'wb') as f:
        r = requests.get('https://identifyus.org/en/cases/' + str(case_id) + '/')
        b = BeautifulSoup(r.text)
        for b in r.iter_content(1024):
            f.write(b)
    return case_html
    


namus_scrape(range(0, 16000))
