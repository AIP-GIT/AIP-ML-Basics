# Hosing price california UI
import streamlit as st
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

st.title("House Price prediction APP")
age = st.sidebar.slider('Hose Age(Years) : ', 0, 60, 5)
st.sidebar.write("Hose Age(Years) ",age)

st.subheader("Numeric input")
number = st.number_input('Insert a number')
st.write('The current number is ', number)