import streamlit as st
import requests

api_url = st.secrets['API_URL']

st.markdown("""

# First Page

## Is it rigth?

            """)


island = st.selectbox('island:', ["Biscoe", "Dream", "Torgersen"])
bill_length_mm = st.number_input('bill_length_mm:')
bill_depth_mm = st.number_input('bill_depth_mm:')
flipper_length_mm = st.number_input('flipper_length_mm:')
body_mass_g = st.number_input('body_mass_g:')
sex = st.selectbox('sex:', ['Male', 'Female'])


if st.button('PREDICT'):
    var = {
    'island': island,
    'bill_length_mm': bill_length_mm,
    'bill_depth_mm': bill_depth_mm,
    'flipper_length_mm': flipper_length_mm,
    'body_mass_g': body_mass_g,
    'sex': sex
    }

    response = requests.get(api_url ,params=var)
    result = response.json()
    st.write(result['prediction'])
