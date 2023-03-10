import streamlit as st
import pandas as pd
import numpy as np
import joblib
import math
import time
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_pickle("data/score_df.pkl")

st.set_page_config(
    page_title = "Car Accident Prediction",
    page_icon="π",
    layout="centered")

st.title('λ³μ μ€μ μ ν΅ν΄ κ΅ν΅μ¬κ³ μνλ μμΈ‘νκΈ°π¨')

st.markdown('##')
st.subheader('λ³μ μ ν')

feat_dict = {'NPA_CL':[],'EVT_CL_CD':[], 'κ°μλ':[],'νμ':[],'μ΅λ':[],'μ μ€':[],'μ μ΄λ':[],'μ§λ©΄μ¨λ':[],'μμ ':[]}


col1, col2 = st.columns(2)
with col1:
    #κ²½μ°°μ²­ κ΅¬λΆ
    feat_dict['NPA_CL'].append(st.selectbox('κ²½μ°°μ²­ κ΅¬λΆ', ['μΆ©λ¨μ²­','λμ μ²­','μΈμ’μ²­']))
    
    #μ΅λ : 0 ~ 100
    feat_dict['μ΅λ'].append(st.slider('μ΅λ',0,100,0,1))
    
    #μ μ€ : 0 ~ 13
    feat_dict['μ μ€'].append(st.slider('μ μ€',0,13,0,1))

    #κ°μλ : 0 ~ 60
    feat_dict['κ°μλ'].append(st.slider('κ°μλ',0,60,0,1))
    
    #νμ : 0 ~ 13
    feat_dict['νμ'].append(st.slider('νμ',0,13,0,1))
    
with col2:
    #μ¬κ±΄μ’λ³μ½λ
    feat_dict['EVT_CL_CD'].append(st.selectbox('μ¬κ΅μ ν', ["κ΅ν΅μ¬κ³ ","μμ£Όμ΄μ ","κ΅ν΅λΆνΈ","κ΅ν΅μλ°","μΈνΌλμ£Ό","μ¬λ§.λνμ¬κ³ "]))
    
    #μ μ΄λ : 0 ~ 10
    feat_dict['μ μ΄λ'].append(st.slider('μ μ΄λ',0,10,0,1))
    
    #μ§λ©΄μ¨λ : -12 ~ 60
    feat_dict['μ§λ©΄μ¨λ'].append(st.slider('μ§λ©΄μ¨λ',-12,60,0,1))
    
    #μμ : 3~6500
    feat_dict['μμ '].append(st.slider('μμ ',3,6500,0,1))
    
resp_data = pd.DataFrame(feat_dict)

st.write("μμΈ‘μ μ¬μ©λ  λ³μ")
st.dataframe(resp_data)

NPA_CL_dic = {"μΆ©λ¨μ²­":19, "λμ μ²­":13,"μΈμ’μ²­": 31}
EVT_CL_CD_dic = {"κ΅ν΅μ¬κ³ ":401,"μμ£Όμ΄μ ":406,"κ΅ν΅λΆνΈ":402,"κ΅ν΅μλ°":403,"μΈνΌλμ£Ό":405,"μ¬λ§.λνμ¬κ³ ":404}

test_data = pd.DataFrame(df.iloc[0]).T
test_data.drop('score', axis = 1, inplace=True)
test_data['RPTER_SEX'] = 3.0

for a in test_data.columns[-7:]:
    test_data[a] = feat_dict[a]
    
test_data['NPA_CL'] = NPA_CL_dic[feat_dict['NPA_CL'][0]]
test_data['EVT_CL_CD'] = EVT_CL_CD_dic[feat_dict['EVT_CL_CD'][0]]

st.write("λ³νλ λ³μ")
st.dataframe(test_data)



if st.button("μμΈ‘νκΈ°"):
    X = df.iloc[:,:-1]
    y = df['score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor()
    with st.spinner('Wait for it...'):
        model.fit(X_train, y_train)
        valid_predict = model.predict(X_test)
        result = model.predict(test_data)
    answer = result[0]
#     st.write("Validation RMSE': ", math.sqrt(mean_squared_error(valid_predict, y_test)))
    st.subheader(f'λͺ¨λΈλ‘ μμΈ‘ν κ²°κ³Ό νμ¬ κ΅ν΅μ¬κ³  μνλ λ²¨μ {round(answer,2)} μλλ€.')
    
    if answer < 4:
        st.write('λΉκ΅μ  μμ ν©λλ€')
    elif answer > 9:
        st.write('λ§€μ° μνν©λλ€!!!')
    else:
        st.write('μ£ΌμνμμΌ ν©λλ€!')
        
    col1, col2, col3 = st.columns([1, 10, 1])
    with col1:
        st.write(' ')

    with col2:
        if answer < 4:
            st.image('img/safe.png')
        elif answer > 9:
            st.image('img/dangerous.png')
        else:
            st.image('img/caution.png')

    with col3:
        st.write(' ')
    
    
    
