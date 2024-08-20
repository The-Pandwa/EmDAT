import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv(r'public_emdat.csv')
df

st.map(df)
