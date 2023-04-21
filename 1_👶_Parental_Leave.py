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

# load data
# some text about data loading or something
data_load_state = st.text('Loading data...')
# read in dataframes
df_parental_leave, df_dictionary = read_data()
# remove nan cols
df_parental_leave = df_parental_leave[["Company", "Industry", "Paid Maternity Leave", "Unpaid Maternity Leave", "Paid Paternity Leave", "Unpaid Paternity Leave"]]
# notify when data loading is done
data_load_state.text('Loading data...Done!')

# write what this analysis is even about
st.write("**This is a smaple dataset to practice descriptive data analytics using streamlit.**")
st.write("Each record contains the company's name & industry, \
         as well as crowdsourced information on the paid & \
         unpaid weeks off they offer as part of both their maternity & \
         paternity leave policies (when available)")

# separate industry and sub insdustry
df_parental_leave[['Industry','Sub-industry']] = df_parental_leave['Industry'].str.split(':',expand=True)

# descriptive statistics
# header for descriptive statistics
st.subheader(":bar_chart: Descriptive Statistics")
descriptive = df_parental_leave.describe()
st.write(descriptive)

# group by company
df_parental_leave_gb_company = (df_parental_leave.groupby([df_parental_leave["Company"], df_parental_leave["Industry"]])["Paid Maternity Leave", "Unpaid Maternity Leave", "Paid Paternity Leave", "Unpaid Paternity Leave"].mean())
df_parental_leave_gb_company = df_parental_leave_gb_company.reset_index()

# group by industry
df_parental_leave_gb_industry = (df_parental_leave.groupby([df_parental_leave["Industry"]])["Paid Maternity Leave", "Unpaid Maternity Leave", "Paid Paternity Leave", "Unpaid Paternity Leave"].mean())
df_parental_leave_gb_industry = df_parental_leave_gb_industry.reset_index()

# header for dataframe tabs by compnay
st.subheader(":calendar: Most Parental Leave by Company")

# dataframe tabs
tab_c_p_mat, tab_c_up_mat, tab_c_p_pat, tab_c_up_pat = st.tabs(["Paid Maternity", "Upaid Maternity", "Paid Paternity", "Unpaid Paternity"])

# streamlit dataframe
with tab_c_p_mat:
    st.dataframe(df_parental_leave_gb_company.sort_values(by=['Paid Maternity Leave'], ascending=False), use_container_width=True)
with tab_c_up_mat:
    st.dataframe(df_parental_leave_gb_company.sort_values(by=['Unpaid Maternity Leave'], ascending=False), use_container_width=True)
with tab_c_p_pat:
    st.dataframe(df_parental_leave_gb_company.sort_values(by=['Paid Paternity Leave'], ascending=False), use_container_width=True)
with tab_c_up_pat:
    st.dataframe(df_parental_leave_gb_company.sort_values(by=['Unpaid Paternity Leave'], ascending=False), use_container_width=True)


# header for dataframe tabs by industry
st.subheader(":calendar: Most Parental Leave by Industry")

# dataframe tabs
tab_i_p_mat, tab_i_up_mat, tab_i_p_pat, tab_i_up_pat = st.tabs(["Paid Maternity", "Upaid Maternity", "Paid Paternity", "Unpaid Paternity"])

# streamlit dataframe
with tab_i_p_mat:
    st.dataframe(df_parental_leave_gb_industry.sort_values(by=['Paid Maternity Leave'], ascending=False), use_container_width=True)
with tab_i_up_mat:
    st.dataframe(df_parental_leave_gb_industry.sort_values(by=['Unpaid Maternity Leave'], ascending=False), use_container_width=True)
with tab_i_p_pat:
    st.dataframe(df_parental_leave_gb_industry.sort_values(by=['Paid Paternity Leave'], ascending=False), use_container_width=True)
with tab_i_up_pat:
    st.dataframe(df_parental_leave_gb_industry.sort_values(by=['Unpaid Paternity Leave'], ascending=False), use_container_width=True)



