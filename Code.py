import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv(r'public_emdat.csv')
df

geo = df[df['Latitude'].notna()][['Latitude', 'Longitude']]
geo

st.map(geo)
