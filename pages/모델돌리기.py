import streamlit as st
import pandas as pd
import numpy as np
import joblib

df = pd.read_pickle("data/score_df.pkl")

st.set_page_config(
    page_title = "Car Accident Prediction",
    page_icon="🚗",
    layout="wide")

st.title('변수 설정을 통해 교통사고위헙도 예측하기🚨')

st.markdown('##')
st.subheader('변수 선택')

feat_dict = {'NPA_CL':[],'EVT_CL_CD':[], '강수량':[],'풍속':[],'습도':[],'적설':[],'전운량':[],'지면온도':[],'시정':[]}


col1, col2 = st.columns(2)
with col1:
    #경찰청 구분
    feat_dict['NPA_CL'].append(st.selectbox('경찰청 구분', ['충남청','대전청','세종청']))
    
    #습도 : 0 ~ 100
    feat_dict['습도'].append(st.slider('습도',0,100,0,1))
    
    #적설 : 0 ~ 13
    feat_dict['적설'].append(st.slider('적설',0,13,0,1))

    #강수량 : 0 ~ 60
    feat_dict['강수량'].append(st.slider('강수량',0,60,0,1))
    
    #풍속 : 0 ~ 13
    feat_dict['풍속'].append(st.slider('풍속',0,13,0,1))
    
with col2:
    #사건종별코드
    feat_dict['EVT_CL_CD'].append(st.selectbox('사교유형', ["교통사고","음주운전","교통불편","교통위반","인피도주","사망.대형사고"]))
    
    #전운량 : 0 ~ 10
    feat_dict['전운량'].append(st.slider('전운량',0,10,0,1))
    
    #지면온도 : -12 ~ 60
    feat_dict['지면온도'].append(st.slider('지면온도',-12,60,0,1))
    
    #시정: 3~6500
    feat_dict['시정'].append(st.slider('시정',3,6500,0,1))
    
resp_data = pd.DataFrame(feat_dict)

st.write("예측에 사용될 변수")
st.dataframe(resp_data)

NPA_CL_dic = {"충남청":19, "대전청":13,"세종청": 31}
EVT_CL_CD_dic = {"교통사고":401,"음주운전":406,"교통불편":402,"교통위반":403,"인피도주":405,"사망.대형사고":404}

test_data = pd.DataFrame(df.iloc[0]).T
test_data.drop('score', axis = 1, inplace=True)
test_data['RPTER_SEX'] = 3.0

for a in test_data.columns[-7:]:
    test_data[a] = feat_dict[a]
    
test_data['NPA_CL'] = NPA_CL_dic[feat_dict['NPA_CL'][0]]
test_data['EVT_CL_CD'] = EVT_CL_CD_dic[feat_dict['EVT_CL_CD'][0]]

st.write("변환된 변수")
st.dataframe(test_data)
