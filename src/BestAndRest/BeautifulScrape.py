"""Acquisition of information on NHL Draft first overall picks.

Utilizing BeautifulSoup to scrape data from NHL records website. 

Returns:
nhlscraper: class method that uses BeautifulSoup to scrape nhl records website and land it in pandas.

"""
import lxml 
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup 
import requests


class Scrape:
    """ Creates scraper for hockey reference website

    Returns:
    Htmler: requests site html doc contents
    Hockey_scraper: scrape (NH)chel data from html of hockey reference website
    """
    
    def __init__(self, websiteurl):
        """ Build client to make request from website

        Args:
           
            websiteurl(str): url of chosen website

        Returns:
            set requests client to send request for html content
        """
        self.response = requests.get(websiteurl)

    def htmler(self):
        """
        request and display html text of website 
        uses client created with self.response

        Args: 
        self: response client 

        Returns: html text of selected website if request is granted 
        """
        if self.response.ok:
            return self.response.content
        else:
            raise Exception('Request Denied') 

    def hockey_scraper(self):
        """  
            uses the html text as input into beautiful soup scraper
            beautiful soup scraper extracts data from specified html string

            Args: requests client

            Returns:
            data from nhl draft first pick  table on hockey reference 
            """

        soup = BeautifulSoup(self.response.content, "html.parser")
        tableinfo = soup.find('table').text
        return tableinfo
    
    
    


    













        


