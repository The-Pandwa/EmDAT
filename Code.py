import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import folium

df = pd.read_csv(r'public_emdat.csv')

geo = df[df['Latitude'].notna()][['Latitude', 'Longitude']]

st.map(geo,
    latitude='Latitude',
    longitude='Longitude',
    use_container_width=True
    )

point = geo.iloc[0:1]
point

# Créer une carte Folium centrée sur le point sélectionné
m = folium.Map(location=[point['Latitude'].values[0], point['Longitude'].values[0]], zoom_start=10)

# Ajouter un marqueur pour ce point
folium.Marker(
    location=[point['Latitude'].values[0], point['Longitude'].values[0]],
    popup="First Point"
).add_to(m)

# Afficher la carte Folium dans Streamlit
st_folium(m, width=700, height=500)

