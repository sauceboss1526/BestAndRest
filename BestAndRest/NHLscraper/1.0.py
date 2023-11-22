""" Infrences and insight from NHL first round picks and their data on the open internet.



 Player statistics from obtained dataset is landed in Excel Workbook file and then converted to csv files. 

 

 rookiesdata -->  List of rookies amd their respective draft information.

                    -Draft Information includes:

                    -draft: Year player was selected in NHL draft. Datatype: integer.

                    -player: Name of selected player. Datatype: string object.
                    
                    -team: The team that selected the player in NHL draft and the location in which franchiose is based. Datatype: string object.
                    
                    -amateur_league: League in which player competed in before NHL. Datatype: string object. Group the count of first overall picks by Amateur League to see which leagues have developed the most first overall picks. Within the top Amateur leagues we can look for the teams that produced the most NHL draft first overall picks
                    
                    -amatuer_team: Name of the team on which the player competed on in Amateur League. Datatype: string object. Find which amateur teams have produced the most first overall picks.                 

                    returns:
                    
                    shapeinfo: size of dataframe
                    nullscounts: count of null values in dataset 
                    describedf: statistical summary of numerical features 
                    
                    
"""
import pandas as pd
import numpy as np 
import bs4 
from bs4 import BeautifulSoup

class scrape:
    def __init__(self, htmlscript):
        self.htmlp = htmlscript



import seaborn as sns 
import matplotlib.pyplot as plt

class intro

