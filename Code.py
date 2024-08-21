import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

df = pd.read_csv(r'public_emdat.csv')

geo = df[df['Latitude'].notna()][['Latitude', 'Longitude']]

st.map(geo,
    latitude='Latitude',
    longitude='Longitude',
    zoom = 0?
    size = 100
    )
