import streamlit as st
from pathlib import Path
import os
import os.path
import glob
from PIL import Image

def app():
    buttonstat=st.button('Get Results', disabled=False)
    if buttonstat:
        piclist=[]
        for i in (glob.glob("./results/*.png")):
            piclist.append(i)
        print(piclist)
        image = Image.open(piclist[0])
        st.image(image)
        image1 = Image.open(piclist[1])
        st.image(image1)
        image2 = Image.open(piclist[2])
        st.image(image2)
