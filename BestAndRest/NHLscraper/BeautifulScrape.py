"""Acquisition of information on NHL Draft first overall picks.

Utilizing BeautifulSoup to scrape data from NHL records website. 

returns:
nhlscraper: class method that uses BeautifulSoup to scrape nhl records website and land it in pandas.

"""
import lxml 
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup 
import requests


class scrape:
    def __init__(self, websiteurl):
        self.response = requests.get(websiteurl)

    def htmler(self):
        if self.response.ok:
            return self.response.content
        else:
            raise Exception('Request Denied') 

    def scrapechel(self):
        soup = BeautifulSoup(self.response.content, "html.parser")
        tableinfo = soup.find('table').text
        return tableinfo
    
    
    


    













        


