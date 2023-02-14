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
- __시군구__ : 충남, 대전, 세종
- __사망자수__ : 0, 1, 2, 3 (명)
- __중상자수__ : 0, 1, 2, 3, 4, 5, 6, 15 (명
- __경상자수__ : 1 ~ 19 (명)
- __부상신고자수__ : 0 ~ 6, 29(명)
- __사고유형__ : '차대차 - 측면충돌', '차대차 - 기타', '차대차 - 추돌', '차대사람 - 기타', '차대사람 - 횡단중', '차대차 - 정면충돌', '차대차 - 후진중충돌', '차대사람 - 차도통행중', '차대사람 - 길가장자리구역통행중', '차대사람 - 보도통행중'
- __법규위반__ : '안전운전불이행', '신호위반', '안전거리미확보', '교차로운행방법위반', '중앙선침범', '보행자보호의무위반', '직진우회전진행방해', '기타', '차로위반', '불법유턴', '과속'
- __노면상태__ : EXPERIENCE IN CURRENT FIELD
- __기온__ : EXPERIENCE IN CURRENT FIELD
- __강수량__ : EXPERIENCE IN CURRENT FIELD
- __풍속__ : EXPERIENCE IN CURRENT FIELD
- __풍향__ : EXPERIENCE IN CURRENT FIELD
- __습도__ : EXPERIENCE IN CURRENT FIELD
- __적설__ : EXPERIENCE IN CURRENT FIELD
- __전운량__ : EXPERIENCE IN CURRENT FIELD
- __지면온도__ : EXPERIENCE IN CURRENT FIELD
- __시정__ : EXPERIENCE IN CURRENT FIELD

''')
