import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import folium
from streamlit_folium import st_folium


df = pd.read_csv(r'public_emdat.csv')

# Afficher la carte avec st.map
st.map(df[df['Latitude'].notna()][['Latitude', 'Longitude']],
    latitude='Latitude',
    longitude='Longitude',
    use_container_width=True
      )

# Créer une carte Folium centrée sur le premier point de geo
m = folium.Map(location=[df.iloc[0]['Latitude'], df.iloc[0]['Longitude']], zoom_start=2)

# Ajouter des marqueurs pour chaque point
for _, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"'Disaster Type'"
    ).add_to(m)

# Afficher la carte Folium dans Streamlit
st_folium(m, width=700, height=500)
