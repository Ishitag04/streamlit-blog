import streamlit as st

st.title("WIDGETS")

if st.button("Subscribe"):
    st.write("Like this video too")

name = st.text_input("Name")
st.write(name)

address = st.text_area("Enter your address")
st.write("Your address is ",address)

data = st.date_input("Enter a date")

time = st.time_input("Enter a time")

if st.checkbox("You accept the T&C", value=True):
    st.write("Thank you")

v1 = st.radio("Colors",["Red","Green", "Blue"], index=1)

v2 = st.selectbox("Colors",["r","b","g"],index=0)

st.write(v1,v2)

v3 = st.multiselect("Colors",["a","b","c"])

st.write(v3)

st.slider("age",min_value=18, max_value=80, value=30,step=2)

st.number_input("numbers", min_value=18, max_value=80, value=30, step=2)

img = st.file_uploader("Upload a file")
st.image(img)




