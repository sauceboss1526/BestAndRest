"""Acquisition of information on traffic violation data.

Utilizing access to the City of New York API 

Returns: a pandas dataframe of traffic violation data that can be downloaded by the "last" apic class method.
A unique feature about the City of New York API is that it has unique endpoints to receive data in csv format for each dataset.


"""

%pip install sodapy

import pandas as pd 
import csv
from sodapy import Socrata

class apic:
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

        endpointdf(str): the dataset url in the api 

        records (int): desired number of records to return

        name(str): the name to assign to csv file containing traffic violations data ending in '.csv'. 

        returns: Popuulated Pandas DataFrame object with data from API

        """
        data = self.get(endpointdf, records)
        resultados = pd.DataFrame.from_records(data)
    
        newcsv = resultados.to_csv(name)
        return resultados