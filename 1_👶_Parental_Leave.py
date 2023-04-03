# -*- coding: utf-8 -*-
"""
Parental Leave

Created on Sun Apr  2 20:28:40 2023

@author: ryantvackner
"""


# import libaries
import pandas as pd
import streamlit as st
import heapq

st.set_page_config(
    page_title = "Prental Leave Analysis",
    page_icon = ":baby:"
    )

# add that cache money
# read data
@st.cache_data
def read_data():
    # list of csv 
    ls_loc = ["parental_leave.csv", "data_dictionary.csv"]
    df = []
    for loc in ls_loc:
        df.append(pd.read_csv("https://raw.githubusercontent.com/ryantvackner/parental-leave/master/parental_company_leave/" + loc, encoding = 'unicode_escape'))
    return df



# title of app
st.title(":baby: Parental Leave Analysis")
st.caption("Created by: Ryan T Vackner")

# some text about data loading or something
data_load_state = st.text('Loading data...')
# read in dataframes
df_parental_leave, df_dictionary = read_data()
df_parental_leave = df_parental_leave[["Company", "Industry", "Paid Maternity Leave", "Unpaid Maternity Leave", "Paid Paternity Leave", "Unpaid Paternity Leave"]]
# notify when data loading is done
data_load_state.text('Loading data...Done!')


# descriptive statistics
df_parental_leave.describe()






