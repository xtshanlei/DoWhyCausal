import streamlit as st
import pandas as pd
st.title('Automatic Causality')
st.subheader('by Yulei')
st.image('causal_graph.png')
uploaded_file = st.file_uploader("Upload your dataset:")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.dataframe(df)
    all_columns = st.multiselect('Please choose the columns that you want to include',df.columns)
    st.write(all_columns)
    training=df[all_columns].copy()
    st.dataframe(training)
    causal_graph= st.text_area('Please input the graph text',''' ''')
    if causal_graph:
        treatment = st.selectbox("What's your treatment?",all_columns)
        output = st.selectbox("What's your output?",all_columns)
        if treatment and output:
            from dowhy import CausalModel
            model= CausalModel(
                    data = training,
                    graph=causal_graph.replace("\n", " "),
                    treatment=treatment,
                    outcome=output,)
            st.image('causal_graph.png')
