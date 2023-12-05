""" utilizing xml parsing to extract rocketfire into Israel data from the open internet

returns: pandas dataframe with rocketfire data
"""

import pandas as pd
import numpy as np
import requests
from xml.etree import ElementTree

class xmlpy:
    """returns 
    """
    def xmlparsing(self):
        response = requests.get('https://www.jewishvirtuallibrary.org/palestinian-rocket-and-mortar-attacks-against-israel')
        if response.ok:
            return root = ElementTree.fromstring(response.content)
            else:
                raise Exception('Could not parse')
