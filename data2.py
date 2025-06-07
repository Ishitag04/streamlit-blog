import streamlit as st
import pandas as pd
import numpy as np
import time

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape(2,4)
dic = {
    "name" : "Harsh",
    "age" : 21,
    "city" : "Noida"
}

data = pd.read_csv("Salary_Data.csv")
print(data)

st.dataframe(a)
st.dataframe(n)
st.dataframe(nd)
st.dataframe(dic)
st.dataframe(data)
st.dataframe(data, height=200, width=500)

st.table(data) #It displays all the data, in case of st.dataframe scrollbar was coming for large data
# So table is beneficial for small data

st.table(a)
st.table(dic)

st.json(dic)

st.write(data)
st.write(a)
st.write(dic)

@st.cache_data
def ret_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))