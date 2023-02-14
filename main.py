import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import seaborn as sns

st.set_page_config(layout="wide")
# For EDA
df = pd.read_pickle('data/taas+weather.pkl')

st.title("기상별 교통사고 위험율 예측")
st.header("추음새 조")
st.header("About the Data")

st.markdown('##')
st.subheader('Dataset Sample')
st.write(df.head())

a = st.selectbox( 'Select Feature', ['사망자수', '중상자수', '경상자수', '부상신고자수', '사고유형', '법규위반','기상상태', '도로형태'])
if a in ['사망자수', '중상자수', '경상자수', '부상신고자수']:
    desc = pd.DataFrame(df[a].describe()).T
    st.dataframe(desc)
else:
    desc = pd.DataFrame(df[a].value_counts()).T
    st.dataframe(desc)
  
