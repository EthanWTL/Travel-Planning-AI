import pandas as pd # type: ignore
from pandas import DataFrame # type: ignore
from typing import List
from difflib import get_close_matches

class Restaurants:
    def __init__(self, path = "../Datasets/Restaurants_task1.csv"):
        self.path = path
        self.data = pd.read_csv(self.path)

    def run(self,
            budget: str,
            cuisine: str,
            preference: List[str]
            ) -> DataFrame: #Cheap Budget, Indian, [Good Flavor, Good Value]
        
        #buget
        price_map = {'cheap budget':['$','$$'],'moderate budget':['$','$$','$$$'],'expensive budget':['$$','$$$','$$$$']}
        price_limit = price_map[budget.lower()]
        result = self.data[self.data['price'].isin(price_limit)]
        
        #cuisine
        if cuisine == 'US':
            cuisine = ['American','American (New)','American (Traditional)']
        else:
            cuisine = [cuisine]

        result = result[(result['cuisine_1'].isin(cuisine)) | (result['cuisine_2'].isin(cuisine))]

        #preference        
        for pref in preference:
            #print(pref)
            prefs = pref.split(' ')
            col = prefs[1].lower()
            #print(col)
            if col not in self.data.columns:
                col = get_close_matches(col, self.data.columns, n=1, cutoff=0.6)  
            #print(col)
            pref_list = ['good ' + col, 'excellent ' + col]
            result = result[result[col].isin(pref_list)]

        result.to_csv('test_csv.csv', index=False)
        return result