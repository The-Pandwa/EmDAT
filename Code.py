import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import folium
from streamlit_folium import st_folium


df = pd.read_csv(r'public_emdat.csv')

geo = df[df['Latitude'].notna()][['Latitude', 'Longitude']]

st.map(geo,
    latitude='Latitude',
    longitude='Longitude',
    use_container_width=True
      )

# Créer une carte Folium centrée sur le point sélectionné
m = folium.Map(location=[geo['Latitude'].values[0], geo['Longitude'].values[0]], zoom_start=1)

# Ajouter un marqueur pour ce point
folium.Marker(
    location=[geo['Latitude'].values[0], geo['Longitude'].values[0]],
    popup="First Point"
).add_to(m)

# Afficher la carte Folium dans Streamlit
st_folium(m, width=700, height=500)

