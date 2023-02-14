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
    desc = pd.DataFrame(df[a].value_counts())
    st.dataframe(desc)
    
st.markdown('##')
st.subheader('Check Graph')
c = st.selectbox( 'Select Graph', ['사고유형별 사망자수 비율'])
if c == '사고유형별 사망자수 비율':
    tmp = df.groupby('사고유형').sum()[['사망자수', '중상자수','경상자수']]
    tmp['death_ratio'] = tmp['사망자수']/(tmp['사망자수'] + tmp['중상자수'] + tmp['경상자수'])
    tmp['death_ratio'] = tmp['death_ratio'] * 100
    fit = px.bar(data_frame=tmp,
                 x = tmp['death_ratio'].sort_values(ascending=False).index,
                 y = tmp['death_ratio'].sort_values(ascending=False),
                 color = tmp['death_ratio'].sort_values(ascending=False).index
                )
    st.plotly_chart(fig)