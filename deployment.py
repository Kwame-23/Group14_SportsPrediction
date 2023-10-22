from sklearn.metrics import mean_absolute_error
import streamlit as st 
import pandas as pd
import pickle
import numpy as np



st.title("Something Prediction")
st.markdown("\n\n\n\n\n\n")
l, m ,r = st.columns(3)

with l:
    shooting = st.number_input("Shooting", min_value=15,max_value=99)
    mentality_vision = st.number_input("Vision", min_value=15,max_value = 99)
    attacking_short_passing= st.number_input("Attacking short passing ", min_value=15, max_value=99)
    physic= st.number_input("Physical ", min_value=15,max_value = 99)
    value_eur= st.number_input("Value($)", min_value=0.0)

with m:
    passing = st.number_input("Passing", min_value=15,max_value=99)
    mentality_composure = st.number_input("Composure", min_value=15,max_value=99)
    power_shot_power= st.number_input("Shot Power ", min_value=15,max_value=99)
    age= st.number_input("Age ", min_value=15, max_value=60)
    release_clause_eur= st.number_input("Release Clause($)", min_value=0.0)
    
with r:
    dribbling = st.number_input("Dribbling", min_value=15,max_value=99)
    movement_reactions = st.number_input("Reaction", min_value=15,max_value=99)
    potential= st.number_input("Potential ", min_value=15,max_value=99)
    wage_eur= st.number_input("Wage($)", min_value=0.0)
    
    
    
st.markdown("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

x = st.button("Predict")



model = pickle.load(open('model.pkl','rb'))

    




    
attributes= np.array([[value_eur,shooting,passing,dribbling,physic,movement_reactions,mentality_composure,potential,power_shot_power,release_clause_eur,wage_eur,mentality_vision,age,attacking_short_passing]
                     ])





    
#x = st.button("Predict")
if x:
    #run the model and return predictions
    #predict confidence as well
    st.balloons()

    ypred=model.predict(attributes)
    st.success(f"The overall rating of your player is **{ypred}**")
    st.balloons()
    
