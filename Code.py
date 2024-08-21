import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

df = pd.read_csv(r'public_emdat.csv')

geo = df[df['Latitude'].notna()][['Latitude', 'Longitude']]

st.map(geo,
    latitude='Latitude',
    longitude='Longitude'
    )

# Ajouter une colonne pour les infobulles (par exemple, une description ou un autre champ)
geo['info'] = "Point (" + geo['Latitude'].astype(str) + ", " + geo['Longitude'].astype(str) + ")"

# Créer la couche de points avec les infobulles
layer = pdk.Layer(
    'ScatterplotLayer',
    data=geo,
    get_position='[Longitude, Latitude]',
    get_color='[200, 30, 0, 160]',
    get_radius=200,
    pickable=True,
    auto_highlight=True,
    tooltip=True,
)

# Configurer la vue de la carte
view_state = pdk.ViewState(
    latitude=geo['Latitude'].mean(),
    longitude=geo['Longitude'].mean(),
    zoom=3,
    pitch=50,
)

# Créer la carte avec pydeck
r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{info}"}
)

# Afficher la carte avec Streamlit
st.pydeck_chart(r)
