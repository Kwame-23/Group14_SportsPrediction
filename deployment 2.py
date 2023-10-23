
import streamlit as st 
import pandas as pd
from pickle import load
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor








st.title("Fifa Player Overall Rating (⚽️) ")
st.subheader("Input the following features:")
st.text("By Kwadjo and Kwame")
st.markdown("\n\n\n\n\n\n")
l, m ,r = st.columns(3)

with l:
    shooting = st.number_input("Shooting", min_value=15.0,max_value=99.0)
    mentality_vision = st.number_input("Vision", min_value=15.0,max_value = 99.0)
    attacking_short_passing= st.number_input("Attacking short passing ", min_value=15.0, max_value=99.0)
    physic= st.number_input("Physical ", min_value=15.0,max_value = 99.0)
    value_eur= st.number_input("Value($)", min_value=0.0)

with m:
    passing = st.number_input("Passing", min_value=15.0,max_value=99.0)
    mentality_composure = st.number_input("Composure", min_value=15.0,max_value=99.0)
    power_shot_power= st.number_input("Shot Power ", min_value=15.0,max_value=99.0)
    age= st.number_input("Age ", min_value=15.0, max_value=60.0)
    release_clause_eur= st.number_input("Release Clause($)", min_value=0.0)
    
with r:
    dribbling = st.number_input("Dribbling", min_value=15.0,max_value=99.0)
    movement_reactions = st.number_input("Reaction", min_value=15.0,max_value=99.0)
    potential= st.number_input("Potential ", min_value=15.0,max_value=99.0)
    wage_eur= st.number_input("Wage($)", min_value=0.0)
    
    
    
st.markdown("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

x = st.button("Predict")



model_ab = load(open('model.pkl','rb'))

scaler = load(open('scaler.pkl','rb'))
    







user_input = pd.DataFrame(np.array([[value_eur,shooting,passing,dribbling,physic,movement_reactions,mentality_composure,potential,power_shot_power,release_clause_eur,wage_eur,mentality_vision,age,attacking_short_passing]
                     ]),columns=['value_eur','shooting','passing','dribbling','physic','movement_reactions','mentality_composure','potential','power_shot_power','release_clause_eur','wage_eur','mentality_vision','age','attacking_short_passing'])

user_input = scaler.transform(user_input)













if x:
    st.balloons()

    ypred=model_ab.predict(user_input)
    st.success(f"The overall rating of your player is **{ypred}**")
    st.balloons()
    
