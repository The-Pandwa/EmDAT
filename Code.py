import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

df = pd.read_csv(r'public_emdat.csv')

geo = df[df['Latitude'].notna()][['Latitude', 'Longitude']]

st.map(geo,
    latitude='Latitude',
    longitude='Longitude',
    use_container_width=True
    )

import folium
m = folium.Map(location=geo,zoom_start=7)
m
