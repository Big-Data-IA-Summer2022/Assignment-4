import streamlit as st
import datetime
import requests
import os
import json
from main_page import MultiApp
from pages import home, model, pics # import your app modules here

st.set_page_config(page_title="Automating Benchmarking of datasets Dashboard", page_icon=":bowtie:", layout="wide", initial_sidebar_state="collapsed")

if 'if_logged' not in st.session_state:
    st.session_state['if_logged'] = False
    st.session_state['access_token'] = ''

logout_button = st.button(label = 'Logout', disabled=False)

if logout_button:
    st.session_state['if_logged'] = False
    

if st.session_state['if_logged'] == False:
    with st.form(key = 'login', clear_on_submit=True):
        st.subheader("Login")
        username = st.text_input('Your Email ✉️')
        password = st.text_input("Your Password", type="password")
        submit = st.form_submit_button("Submit")
        if submit:
            url = "https://damg7245-assignment03-api-xd232aklcq-uc.a.run.app/login"
            payload={'username': username, 'password': password}
            response = requests.request("POST", url, data=payload)
            if response.status_code == 200:
                json_data = json.loads(response.text)
                st.session_state['access_token'] = json_data["access_token"]
                st.session_state['if_logged'] = True
                st.text("Login Successful")
            else:
                st.text("Invalid Credentials ⚠️")

if st.session_state['if_logged'] == True:
    app = MultiApp()
    st.markdown("""
    # Team 4 welcomes you to Automating Benchmarking of datasets dashboard
    """)

    # Add all your application here
    app.add_app("Home", home.app)
    app.add_app("Model-Test", model.app)
    app.add_app("Results", pics.app)
    
    # The main app
    app.run()
