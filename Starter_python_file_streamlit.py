#import libraries used in notebbok
#if not present use pip to install the required libraries

# to run streamlit file : "streamlit run [file_name.py]"  in terminal or at file location in cmd.

#streamlit 
import streamlit as st
import pandas as pd 
import numpy as np 
import yfinance as yf
import plotly.express as px
from datetime import date, timedelta

st.title("Stock Dashboard")

ticker=st.sidebar.text_input('Ticker','GOOGL')
start_date=st.sidebar.date_input("Start Date",date.today()-timedelta(days=100))
end_date=st.sidebar.date_input("End date",date.today()-timedelta(days=1))



# Get the data
data = yf.download(ticker, start_date, end_date)

#showing data
st.subheader(ticker)
st.write("Table of contents")
st.table(data.head())


#ploting chart for data 
fig=px.line(data,x=data.index,y=data['Adj Close'],title=ticker)
st.plotly_chart(fig)

#create tabs
pricing_data , fundamental_data , news=st.tabs(["Pricing Data", "Fundamental Data","Top 10 news"])

with pricing_data:
    st.write('Price')

with fundamental_data:
    st.write("Fundamental Data")

with news:
    st.write("Top 10 news")






