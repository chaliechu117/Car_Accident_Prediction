import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import seaborn as sns

st.set_page_config(
    page_title="Car Accident Prediction",
    page_icon="π",
    layout="wide"
)

title_name = []
st.markdown("# κ΅ν΅μ¬κ³  νν©μ μμλ΄μλ€π")
st.header(":blue[by μΆμμ]")

df = pd.read_pickle('data/taas+weather.pkl')
df['μκ°'] = df['μ¬κ³ μΌμ'].apply(lambda x: x.split()[1].split(':')[0])
# Selecting
st.markdown('### μλμ λͺ¨λ  ν­λͺ©μ μλ΅ν΄μ£ΌμΈμ.')
days = st.multiselect('λ¬΄μ¨ μμΌμ΄ κΆκΈν΄μ?', df['μμΌ'].unique())
place = st.multiselect('μ΄λ μ§μ μ΄ κΆκΈν΄μ?', df['μ§μ '].unique())
accident = st.multiselect('μ΄λ€ λ΄μ©μ μ¬κ³ μΈκ°μ?', df['μ¬κ³ λ΄μ©'].unique())
time = st.multiselect('μ΄λ μκ°λκ° κΆκΈνκ°μ?', df['μκ°'].unique())
weather = st.multiselect('μ΄λ€ λ μ¨ μ‘°κ±΄μΈκ°μ?', df['κΈ°μμν'].unique())
new_df = df[(df['μμΌ'].isin(days)) & (df['μ§μ '].isin(place))& (df['μκ°'].isin(time))& (df['μ¬κ³ λ΄μ©'].isin(accident))& (df['κΈ°μμν'].isin(weather))]
st.write(new_df)

st.markdown('---')

# For EDA
# df = pd.read_pickle('data/taas+weather.pkl')
# df['μκ°'] = df['μ¬κ³ μΌμ'].apply(lambda x: x.split()[1].split(':')[0])

# st.header("About the Data")

# st.markdown('##')
# st.subheader('Dataset Sample')
# st.write(df.head())

st.markdown('##')
st.subheader('κΈ°μ ν΅κ³κ°')
a = st.selectbox( 'Select Feature', ['μ¬λ§μμ', 'μ€μμμ', 'κ²½μμμ', 'λΆμμ κ³ μμ', 'μ¬κ³ μ ν', 'λ²κ·μλ°','κΈ°μμν', 'λλ‘νν'])
if a in ['μ¬λ§μμ', 'μ€μμμ', 'κ²½μμμ', 'λΆμμ κ³ μμ']:
    desc = pd.DataFrame(df[a].describe()).T
    st.dataframe(desc)
else:
    desc = pd.DataFrame(df[a].value_counts())
    st.dataframe(desc)
    
st.markdown('##')
st.subheader('Check Graph')
c = st.selectbox( 'Select Graph', ['μ¬κ³ μ νλ³ μ¬λ§μμ λΉμ¨', 'κΈ°μμνλ³ μ¬κ³ νν©'])
if c == 'μ¬κ³ μ νλ³ μ¬λ§μμ λΉμ¨':
    tmp = df.groupby('μ¬κ³ μ ν').sum()[['μ¬λ§μμ', 'μ€μμμ','κ²½μμμ']]
    tmp['death_ratio'] = tmp['μ¬λ§μμ']/(tmp['μ¬λ§μμ'] + tmp['μ€μμμ'] + tmp['κ²½μμμ'])
    tmp['death_ratio'] = tmp['death_ratio'] * 100
    fig = px.bar(data_frame=tmp,
                 x = tmp['death_ratio'].sort_values(ascending=False).index,
                 y = tmp['death_ratio'].sort_values(ascending=False),
                 color = tmp['death_ratio'].sort_values(ascending=False).index
                )
    st.plotly_chart(fig)
    
elif c == 'κΈ°μμνλ³ μ¬κ³ νν©':
    fig = px.histogram(data_frame=df, x = 'κΈ°μμν', color = df['μ¬κ³ μ ν'])
    st.plotly_chart(fig)
    

