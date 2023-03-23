import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import numpy as np
import pickle
import base64


st.write("""

# Churn Prediction App
Customer churn is the proportion of customers that stopped using your company's product or service after 
a certain period of time. Organization must look for a way of incenting customers in order to retain them.

This app predicts the probability of a customer churning using Telco Customer Churn data. 
""")

st.markdown("""
Data source: [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn?select=WA_Fn-UseC_-Telco-Customer-Churn.csv)
""")

st.header("Customer Churn Data")

@st.cache

def dataframe(path):
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    data = pd.read_csv(path)
    return data

churn = dataframe("customer_churn.csv")
st.dataframe(churn)

def select_features():
    gender = st.sidebar.selectbox('gender',('Male','Female'))
    payment_method = st.sidebar.selectbox('PaymentMethod',('Bank transfer (automatic)', 'Credit card (automatic)', 
                                                          'Mailed check', 'Electronic check'))
    monthly_charges = st.sidebar.slider('Monthly Charges', 18.25,118.25, 18.25)
    tenure = st.sidebar.slider('tenure', 0.0,72.0, 0.0)
    
    df = {'gender':[gender], 
          'PaymentMethod':[payment_method],
         "MonthlyCharges":[monthly_charges],
          "tenure":[tenure],
         }
    features = pd.DataFrame(df)
    return features

select_df = select_features()

def heatmap():  
    result = pd.pivot_table(data=churn, index='PaymentMethod', columns='Contract',values='Churn')
    fig = sns.heatmap(result, fmt=".2f")
    plt.title("How does PaymentMethod and Contract type affect churn?",
                 fontfamily="serif", fontweight='bold')
    st.write(fig)

heatmap()

st.markdown("""
- It can be seen that those customers with a month-month contract paying by electronic check has high posiibility to churn.
- Customers with a two-year contract have a very low probability throughout.
""")
