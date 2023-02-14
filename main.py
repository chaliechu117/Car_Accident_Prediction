import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import seaborn as sns

st.set_page_config(layout="wide")
# For EDA
df = pd.read_pickle('data/score_df.pkl')

st.title("Employee Future Prediction")
st.header("LIKELION AI SCHOOL-6th, 조용한사자처럼")
st.header("About the Data")
