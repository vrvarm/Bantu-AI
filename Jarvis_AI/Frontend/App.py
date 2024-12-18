import streamlit as st
import requests
import time

if 'user_input' not in st.session_state:
    st.session_state.user_input = ""
if 'response' not in st.session_state:
    st.session_state.response = ""

st.write("Bantu AI")

st.session_state.user_input = st.text_input("Ravi: ", st.session_state.user_input)

if st.session_state.user_input:
    response = requests.post(('https:/271.0.0.1:5000/get-response/'), json={"text": st.session_state.user_input})

    if response.status_code == 200:
        response_data = response.json()
        st.session_state.response = response_data['response']
    else:
        st.error("Error: Couldn't get response from the server")

if st.session_state.response:
    st.write("Bantu: ", st.session_state.response)
            