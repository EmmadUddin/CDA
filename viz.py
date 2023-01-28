# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:45:09 2023

@author: Hp
"""
import pandas as pd
import streamlit as st

st.header('Billionaire Dataset')
folder=r'C:\Users\Hp\Documents\Emmad\Data Analyst_CDA\Class 2-Python for DS/'
#file='Billionaire.csv'
#filepath=folder+file
# reading the file 
df=pd.read_csv('Billionaire.csv') #fro github put the name of orignial file
df['NetWorth']=df['NetWorth'].apply(lambda x: float(x.replace('$', '').replace(' B', '')))

#columns scnee
all_country = sorted(df['Country'].unique())
col1,col2= st.columns(2)

#display on streamlit
selected_country=col1.selectbox('Select Country',all_country)
#subset on selected country
subset_country=df[df['Country']==selected_country]

#get unique sources from selected country
source= sorted(subset_country['Source'].unique())

#display multiselect option
selected_source = col1.multiselect('select source',source)

#subset on selected source
subset_source=subset_country[subset_country['Source'].isin(selected_source)]

#Column2
mainstring = '{}-Billionaures'.format(selected_country)
#main.string =selected_country+ '-Billionaire'
col2.header(mainstring)
col2.dataframe(subset_country)
col2.header('Source wise info')
col2.dataframe(subset_source)





#interactivity 
#all_countries=df['Country'].unique()

#selection=st.selectbox('Select Country',all_countries)

#subset=df[df['Country']==selection]

#st.dataframe(subset)



#dataframe vs table. Table has fix format and we can not do sorting.Think like Dataframe as excel sheet
#find count of billionaires by country 

#bill=df.groupby('Country')['Name'].count().sort_values(ascending=False).head(10)
#st.bar_chart(bill)





#find the most source of income
#top_source=df.groupby('Source')['Name'].count().sort_values(ascending=False).head(10)
#st.bar_chart(top_source)
#get the cummuative wealth of bioilionaires belonging to US
#df['NetWorth']=df['NetWorth'].apply(lambda x: float(x.replace('$', '').replace(' B', '')))
#US_Bill=df['Country']=='United States'
#US_Bill_Table=df[US_Bill]
#Cum_Wealth_US=US_Bill_Table['NetWorth'].cumsum()

