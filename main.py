import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import seaborn as sns

st.set_page_config(
    page_title="Car Accident Prediction",
    page_icon="🚗",
    layout="wide"
)

title_name = []
st.markdown("# 날씨 조건에 따른 교통사고 위험율을 예측해보아요 🚘")
st.header(":blue[by 추음새]")

df = pd.read_pickle('data/taas+weather.pkl')

# Selecting
days = st.multiselect('무슨 요일이 궁금해요?', df['요일'].unique())
place = st.multiselect('어느 지점이 궁금해요?', df['지점'].unique())
accident = st.multiselect('어떤 내용의 사고인가요?', df['사고내용'].unique())
# time = st.multiselect('어떤 시간대가 궁금한가요?', df['시간대']unique))
weather = st.multiselect('어떤 날씨?', df['기상상태']unique))
new_df = df[(df['요일'].isin(days)) & (df['지점'].isin(place))& (df['사고내용'].isin(accident))& (df['기상상태'].isin(weather))]
st.write(new_df)

# For EDA
# df = pd.read_pickle('data/taas+weather.pkl')
df['시간'] = df['사고일시'].apply(lambda x: x.split()[1].split(':')[0])

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
c = st.selectbox( 'Select Graph', ['사고유형별 사망자수 비율', '기상상태별 사고현황'])
if c == '사고유형별 사망자수 비율':
    tmp = df.groupby('사고유형').sum()[['사망자수', '중상자수','경상자수']]
    tmp['death_ratio'] = tmp['사망자수']/(tmp['사망자수'] + tmp['중상자수'] + tmp['경상자수'])
    tmp['death_ratio'] = tmp['death_ratio'] * 100
    fig = px.bar(data_frame=tmp,
                 x = tmp['death_ratio'].sort_values(ascending=False).index,
                 y = tmp['death_ratio'].sort_values(ascending=False),
                 color = tmp['death_ratio'].sort_values(ascending=False).index
                )
    st.plotly_chart(fig)
    
elif c == '기상상태별 사고현황':
    fig = px.histogram(data_frame=df, x = '기상상태', color = df['사고유형'])
    st.plotly_chart(fig)
    

