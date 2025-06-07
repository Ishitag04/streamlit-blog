import streamlit as st
import pandas as pd
import numpy as np

st.title("Registration Form")

first,last = st.columns(2)

first.text_input("First Name")
last.text_input("Last Name")

email, mob = st.columns([3,1])
#divides the column in the ratio of 3:1
email.text_input("Email ID")
mob.text_input("Mobile No.")

user,pw, pw2 = st.columns(3)
user.text_input("Enter Username")
pw.text_input("Password", type="password")
pw2.text_input("Confirm password",type="password")


ch, bl, sub = st.columns(3)
if ch.checkbox("I Agree"):
    st.write("You agreed to Terms and Conditions")
if sub.button("Submit"):
    st.success("Submitted successfully")








