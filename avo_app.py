import streamlit as st
import pandas as pd
import plotly.express as px

avocado = pd.read_csv('avocado.csv')
avocado_stats = avocado.groupby('type')['average_price'].mean()
st.dataframe(avocado_stats)

st.header('Line chart by geographies')

with st.form('line_chart'):
    chosen = st.selectbox(label='Geography', options=avocado['geography'].unique())
    modify = st.form_submit_button('Submit')
    if modify:
        filtered_avocado = avocado[avocado['geography'] == chosen]
        fig = px.line(filtered_avocado,
                           x='date', y='average_price',
                           color='type',
                           title=f'Avocado Prices in {chosen}')
        fig.update_layout(xaxis_title="Date", yaxis_title="Average Price")
        st.plotly_chart(fig)
