from urllib import response
import streamlit as st
import json
import requests

st.title('Xeno Calculator')

option = st.selectbox('what operation do you want to perform?',
                        ('Addition', 'Subtraction', 'Multiplication', 'Division'))
st.write("")
st.write("Select the numbers from the slider below")
x = st.slider('Select a value for x', -100, 100)
y = st.slider('Select a value for y', -100, 100)


inputs = {"operation": option, "x": x, "y": y}


if st.button('Calculate'):
    response = requests.post("http://http://192.168.0.225:8501", data = json.json.dumps(inputs))


    st.subheader(f"Response from API = {response.text}")