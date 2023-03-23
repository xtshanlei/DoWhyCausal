import streamlit as st
import pandas as pd
st.title('Automatic Causality')
st.subheader('by Yulei')

uploaded_file = st.file_uploader("Upload your dataset:")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.dataframe(df)
    all_columns = st.multiselect('Please choose the columns that you want to include',df.columns)
    st.write(all_columns)
    training[all_columns]=df[all_columns].copy()
    st.dataframe(training)
