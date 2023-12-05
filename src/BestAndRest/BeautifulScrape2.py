"""Acquisition of information for NHL Draft first overall picks.

Utilizing pandas to scrape data from NHL records website. 

returns:
reader: class method that uses pandas to scrape tablular data from Hockey-References website.

"""
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup 
import requests
import csv 

class Scrape:
    """ Create DataFrame to land scraped data into Pandas DataFrame

        Returns:
            Reader: creates a pandas dataframe object with scraped tabular data.
    """
    def __init__(self, websiteurl):
        """
        Args:
            websiteurl(str): url of chosen website
        Returns:
            landing of tabular data in pandas dataframe 
            
        """
        self.df = pd.read_html(websiteurl)[0]
    
    def reader(self):
        """ Create pandas df object  
        Args:
            dataframe(series): pandas dataframe of tabular data scraped from Hoceky References website
        
        Returns: 
            pandas dataframe object of scraped tabular data from Hockey References website
        
        """
        
        table = self.df
        return table

