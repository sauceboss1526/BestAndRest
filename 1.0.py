""" Infrences and insight from NHL first round picks and their data on the open internet.

Alexis Lafraniere of the New York Rangers is occasionally labeled as a "bust" through media outlets.  
A bust is a player drafted first overall and spends majority of his career playing outside of the NHL (change wording). 
First overall pick data will be gathered from NHL statistics websites via BeautifulSoup to compare first overall NHL picks.
This analysis explores relationships among features related to the player's performance  

 Player statistics from obtained datasets is aggregated in Excel Workbooks and then converted to csv files. 
 -Sample only includes players who have played at least two seasons in the NHL.
 

 Rookiesdata -->  List of rookies amd their respective draft information.
                    -Draft Information includes:
                    -teamcity: Location in which NHL team is based in. Datatype: string
                    -teamname: The team that selected the player in NHL draft. Datatype: string. 
                    -year: Year player was selected in NHL draft. Datatype: integer.
                    -GP: Number of games player played in the NHL. Datatype: integer.
                    -PPG: Sum of goals and assists divided by number of games played. Datatype: float.
                    -G: Total goals scored by player. Datatype: integer.
                    -A: Total goals assisted by player. Datatype: integer.
                    -champion: Boolean indicator if player is a Stanley Cup champion. 1 = player has won Stanley Cup in his career 0 = player never won the Stanley Cup. Datatype: integer                

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

