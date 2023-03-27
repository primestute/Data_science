import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

@st.cache

def dataframe(path):
    data = pd.read_csv(path)
    data = data[(data["bedrooms"] <= 6) & (data["bedrooms"] > 0)]
    data = data.drop(columns="zipcode", axis =1)
    return data

house = dataframe('house_data.csv')
st.dataframe(house)

bedroom = house.bedrooms.value_counts(normalize = True)
st.title("Proportion of bedroom type")
st.bar_chart(bedroom)
st.markdown("- 3 bedrooms is the most common bedroom type.")


# Create the plotly express figure
fig = px.scatter_mapbox(
    house,
    lat="lat",
    lon="long",
    color="price",
    color_discrete_sequence=["blue", "red"],
    zoom=11,
    height=600,
    width=600,
    hover_data=["price"],
)
fig.update_layout(mapbox_style="open-street-map")

# Show the figure
st.plotly_chart(fig, use_container_width=True)
