import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv(r'public_emdat.csv')
df

geo = df[df['Latitude'] != 0]
geo
st.map(geo)
