import streamlit as st
import pandas as pd
st.title('Automatic Causality')
st.subheader('by Yulei')

uploaded_file = st.file_uploader("Upload your dataset:")
if uploaded_file is not None:
    st.dataframe(uploaded_file)
