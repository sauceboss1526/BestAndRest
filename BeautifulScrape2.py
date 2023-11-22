"""Acquisition of information for NHL Draft first overall picks.

Utilizing pandas to scrape data from NHL records website. 

returns:
nhlscraper: class method that uses pandas to scrape table on Hockey-References website.

"""
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup 
import requests
import csv 

class scrape:
    def __init__(self, websiteurl):
        self = pd.read_html(websiteurl)
        rookiesdata1 = self
        return rookiesdata1 
