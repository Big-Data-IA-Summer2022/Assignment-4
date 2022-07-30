from nbformat import write
import streamlit as st
import requests
import json
import tempfile
from pathlib import Path

def app():
    st.markdown("#")
    st.sidebar.header("Automating Benchmarking of datasets")

    st.subheader("This model automates the application so we can trigger a benchmarking task from dataperf using Airflow")
    st.markdown('Please select values to get result :')

    option = st.selectbox('Select Data_ID',('01g317-flipped','04hgtk-flipped','04rky-flipped','09j2d-flipped','01g317'))
    option1 = st.selectbox('Select train_size',('300',))     
    option2 = st.selectbox('Select noice_level',('0.3',)) 
    option3 = st.selectbox('Select test_size',('500',)) 
    option4 = st.selectbox('Select val_size',('100',)) 

    #st.write('You selected:', 'Data_ID:',option,'train_size:', option1,'noice_level:', option2, 'test_size is:', option3, 'val_size is:', option4)


    buttonstat=st.button('Get Results', disabled=False)
    if buttonstat:
        from jinja2 import Environment, FileSystemLoader
        env = Environment(loader = FileSystemLoader(r"C:\Users\Juichavan\Desktop\assign4"), trim_blocks=True, lstrip_blocks=True)

        template = env.get_template('template.yml')

        values = {
                    'data_id': option,
                    'train_size': option1,
                    'noise_level': option2,
                    'test_size': option3,
                    'val_size': option4,
                    'baseline': 'random',

         }
        print(template.render(values))
        file=open("output.yaml", "w")
        file.write(template.render(values))
        file.close()

        st.write("Result Printed Successfully. Please visit terminal and output.yaml file for results")

        
