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
st.markdown('''
The data has following features : 

Independent value
- __시군구__ 
- __사망자수__
- __중상자수__
- __경상자수__ 
- __부상신고자수__ 
- __사고유형__ 
- __법규위반__ 
- __노면상태__ 
- __기온__
- __강수량__ 
- __풍속__
- __풍향__
- __습도__ 
- __적설__ 
- __전운량__ 
- __지면온도__ 
- __시정__ 

''')
