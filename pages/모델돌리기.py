import streamlit as st
import pandas as pd
import numpy as np
import joblib

df = pd.read_pickle("data/score_df.pkl")

st.set_page_config(layout="centered")
st.title('변수 설정을 통해 교통사고위헙도 예측하기')

st.markdown('##')
st.subheader('변수 선태')

#경찰청 구분
NPA_CL_dic = {"충남청":19, "대전청":13,"세종청": 31}
NPA = st.selectbox('경찰청 구분', ['충남청','대전청','세종청'])
location = NPA_CL_dic[NPA]

#사건상태 : "무조건 10으로 넣기"

#사건종별코드
EVT_CL_CD_dic = {"교통사고":401,"음주운전":406,"교통불편":402,"교통위반":403,"인피도주":405,"사망.대형사고":404}

#RPTER_SEX : "무조건 불상"

#강수량 : 0 ~ 60
#풍속 : 0 ~ 13
#습도 : 0 ~ 100
#적설 : 0 ~ 13
#전운량 : 0 ~ 10
#지면온도 : -12 ~ 60
#시정: 3~6500




