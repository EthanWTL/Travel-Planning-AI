import pandas as pd # type: ignore
from pandas import DataFrame # type: ignore
from typing import List
from difflib import get_close_matches


class Attractions:
    def __init__(self, path = "../Datasets/Attractions_task1.csv"):
        self.path = path
        self.data = pd.read_csv(self.path)
        #print("Accommodations loaded.")
    def run(self,
            budget: str,
            preference: List[str]
            ) -> DataFrame: #AttractionSearch[Moderate Budget, [Family Oriented]]
        price_map = {'cheap budget':['$','$$'],'moderate budget':['$','$$','$$$'],'expensive budget':['$$','$$$','$$$$']}
        price_limit = price_map[budget.lower()]
        result = self.data[self.data['price'].isin(price_limit)]
        
        #dealing with the preference, need to change the original dataset.
        # currently, we have family_oriented as the column name, but medium family oriented as the actual value, the llm might switch between

        col = get_close_matches(preference[0].lower(), self.data.columns, n=1, cutoff=0.6)[0]
        pref = col.split('_')[0] + ' ' + col.split('_')[1]
        pref_list = ['medium ' + pref, 'high ' + pref]
        result = result[result[col].isin(pref_list)]
        #result.to_csv('test_csv.csv', index=False)
        return result