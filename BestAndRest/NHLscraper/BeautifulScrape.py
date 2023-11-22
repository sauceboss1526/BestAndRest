"""Acquisition of information on NHL Draft first overall picks.

Utilizing BeautifulSoup to scrape data from NHL records website. 

returns:
nhlscraper: class method that uses BeautifulSoup to scrape nhl records website and land it in pandas.

"""
%pip install lxml
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup 
import requests
import csv 

class scrape:
    def __init__(self, websiteurl):
        self.request = requests.get(websiteurl)


    def scrapechel(self):
        soup = BeautifulSoup(self.request.content, "html.parser")
        table = soup.find('table').text.copy
        return table
    













        


