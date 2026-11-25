import streamlit as st
import requests

"""
# Zoologist front
"""

option_island = st.radio('Select an island', ('Biscoe', 'Dream', 'Torgersen'))

option_bill_length = st.slider('Select the bill length (in mm)', 30, 60, 45)
option_bill_depth = st.slider('Select the bill depth (in mm)', 11, 25, 18)
option_flipper_length = st.slider('Select the flipper length (in mm)', 150, 250, 200)
option_body_mass = st.slider('Select the body mass (in g)', 2500, 6500, 4500)

option_sex = st.radio('Select its sex', ('Male', 'Female'))

dict_params = {
    "island": option_island,
    "bill_length_mm": option_bill_length,
    "bill_depth_mm": option_bill_depth,
    "flipper_length_mm": option_flipper_length,
    "body_mass_g": option_body_mass,
    "sex": option_sex,
}

url_predict = f"https://zoo-api-1067335407750.europe-west1.run.app/predict?island={dict_params['island']}&bill_length_mm={dict_params['bill_length_mm']}&bill_depth_mm={dict_params['bill_depth_mm']}&flipper_length_mm={dict_params['flipper_length_mm']}&body_mass_g={dict_params['body_mass_g']}&sex={dict_params['sex']}"
if st.button('Predict'):
    data = requests.get(url_predict).json()
    st.write(f"We predict with a probability of {round(data['probability'], 2)}% that it is a penguin from the {data['species']} species.")
