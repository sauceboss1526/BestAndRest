"""Acquisition of information for NHL Draft first overall picks.

Utilizing BeautifulSoup to scrape data from NHL records website. 

returns:
nhlscraper: class method that uses BeautifulSoup to scrape nhl records website and land it in a csvfile.

"""
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup 
import urllib.request
import csv 

class intro:
    def __init__(self, websiteurl):
        self.htmldoc = urllib.request.urlopen(websiteurl)
        html = self.htmldoc.read()
        


