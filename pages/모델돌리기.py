import streamlit as st
import pandas as pd
import numpy as np
import joblib

df = pd.read_pickle("data/score_df.pkl")

st.set_page_config(layout="centered")
st.title('변수 설정을 통해 교통사고위헙도 예측하기')

#경찰청 구분
NPA_CL_dic = {"충남청":19, "대전청":13,"세종청": 31}
NPA = st.slider('경찰청 구분'. ['충남청','대전청','세종청'])
location = NPA_CL_dic[NPA]



