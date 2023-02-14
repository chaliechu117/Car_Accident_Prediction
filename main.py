import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import seaborn as sns

st.set_page_config(layout="wide")
# For EDA
df = pd.read_pickle('data/score_df.pkl')

st.title("기상 별 교통사고 위험율 예측")
st.header("추음새 조")
st.header("About the Data")
