import streamlit as st
import pandas as pd
import numpy as np
import joblib

df = pd.read_pickle("data/score_df.pkl")

st.set_page_config(layout="centered")
st.title('변수 설정을 통해 교통사고위헙도 예측하기')

feat_list = df.columns.tolist()



