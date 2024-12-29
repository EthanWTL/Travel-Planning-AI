import pandas as pd # type: ignore
from pandas import DataFrame # type: ignore
from typing import List
from difflib import get_close_matches

class Accommodations:
    def __init__(self, path = "../Datasets/Hotels_task1.csv"):
        self.path = path
        self.data = pd.read_csv(self.path)
        #print("Accommodations loaded.")
    def run(self,
            budget: str,
            preference: List[str]
            ) -> DataFrame: #Cheap budget,[Good Location]
        price_map = {'cheap budget':['$','$$'],'moderate budget':['$','$$','$$$'],'expensive budget':['$$','$$$','$$$$']}
        price_limit = price_map[budget.lower()]
        result = self.data[self.data['price'].isin(price_limit)]
        
        #dealing with the preferences
        #print(preference)
        for pref in preference:
            #print(pref)
            prefs = pref.split(' ')
            col = prefs[1].lower()
            print(col)
            if col not in self.data.columns:
                col = get_close_matches(col, self.data.columns, n=1, cutoff=0.6)[0]
            print(col)
            pref_list = ['good ' + col, 'excellent ' + col]
            result = result[result[col].isin(pref_list)]
        
        #result.to_csv('test_csv.csv', index=False)
        return result
        