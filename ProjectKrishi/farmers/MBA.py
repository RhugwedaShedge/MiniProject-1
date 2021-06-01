#Loading neccesary packages

from django_pandas.io import read_frame
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def apriori_algo():
    myretaildata = pd.read_excel('Krishi_dataset.xlsx')
    

    #Data Cleaning
    myretaildata['Description'] = myretaildata['Description'].str.strip() #removes spaces from beginning and end
    myretaildata.dropna(axis=0, subset=['InvoiceNo'], inplace=True) #removes duplicate invoice
    myretaildata['InvoiceNo'] = myretaildata['InvoiceNo'].astype('str') #converting invoice number to be string
    myretaildata = myretaildata[~myretaildata['InvoiceNo'].str.contains('C')] #remove the credit transactions

    #Separating transactions for Germany
    mybasket = (myretaildata[myretaildata['Country'] =="India"]
            .groupby(['InvoiceNo', 'Description'])['Quantity']
            .sum().unstack().reset_index().fillna(0)
            .set_index('InvoiceNo')) 


    #converting all positive vaues to 1 and everything else to 0
    def my_encode_units(x):
        if x <= 0:
            return 0
        if x >= 1:
            return 1

    my_basket_sets = mybasket.applymap(my_encode_units)
    #my_basket_sets.drop('POSTAGE', inplace=True, axis=1) #Remove "postage" as an item


    #Generatig frequent itemsets
    my_frequent_itemsets = apriori(my_basket_sets, min_support=0.04, use_colnames=True)


    #generating rules
    my_rules = association_rules(my_frequent_itemsets, metric="lift", min_threshold=1)
    print("my_rules",my_rules)

    rules = my_rules[ (my_rules['lift'] >= 1) & (my_rules['confidence'] >= 0.6 ) ]

    print("rules : \n",rules)


    return rules

