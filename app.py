import streamlit as st



st.markdown("""

# First Page

## Is it rigth?

            """)


island = st.text_input('island:')
bill_length_mm = st.text_input('bill_length_mm:')
bill_depth_mm = st.text_input('bill_depth_mm:')
flipper_length_mm = st.text_input('flipper_depth_mm:')
body_mass_g = st.text_input('body_mass_g:')
sex = st.text_input('sex:')
