"""Acquisition of information on traffic violation data.

Utilizing access to the City of New York API 

Returns:
    apic: class that connects and returns to City of New York API
    analysis: analysis of data obtained from City of New York API

"""
import sodapy
import pandas as pd 
import csv
from sodapy import Socrata
import requests
import matplotlib.pyplot as plt
import seaborn as sns
class apic:
    """
    returns:
        results:  Utilizes client to connect to desired dataset in City of New York API for public data
    """
    def __init__(self, endpointurl):
        """
        initializes client to connect to City of New York API for public datasets.

        endpointurl (str): the link to API without reference to a specific public dataset. 
        The API offers datasets that are non-public and require login credentials.

        returns: client that connects to City of New York API for public datasets
        
        """
    self = Socrata(endpointurl, None)

    def results(self, endpointdf, records, name):
        """ 
        Utilizes client to connect to desired dataset in City of New York API for public data

        args:

        endpointdf(str): the dataset url in the api 

        records (int): desired number of records to return

        name(str): the name to assign to csv file containing traffic violations data ending in '.csv'. 

        returns: Populated Pandas DataFrame object with data from API

        """
        data = self.get(endpointdf, records)
        results = pd.DataFrame.from_records(data)
    
        newcsv = results.to_csv(name)
        return results, newcsv

class analysis:
    """Analyzing parking tickets data

    Returns:
    read: read data and create pandas dataframe with parking violations data 
    table1: bar chart of violations per vehicle body type
    table2: bar chart of violations per vehicle make


    """
    def __init__(self, csvname):
        """
        """
        self.df = pd.read_csv(csvname)

    def bar1(self):
        table1 = self.df.groupby('vehicle_body_type').agg(violations =('summons_number', 'count')).reset_index().sort_values(by = 'violations', ascending  = False).head(8)
        fig, ax = plt.subplots(figsize = (16,6))
        sns.barplot(x = 'vehicle_make', y = 'violations', data = table2)
        return plt.show()


    def bar2(self):
        table2 = self.df.groupby('vehicle_make').agg(violations =('summons_number', 'count')).reset_index().sort_values(by = 'violations', ascending  = False).head(8)
        fig, ax = plt.subplots(figsize = (16,6))
        sns.barplot(x = 'vehicle_make', y = 'violations', data = table2)
        return plt.show()
    
    




    


    
