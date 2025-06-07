# import streamlit as st

# st.title("Session State")
# st.header("counter")

# if "counter" not in st.session_state:
#     st.session_state["counter"] = 0

# count = st.session_state.counter

# {
#     "counter" : 1
# }

# if incremet:= st.button("Add 1"):
#     count+=1
#     st.session_state.counter = count
# st.write(count)

#this is the first method:



#session state is a way to share variable values between each rerun that happens
#it is like a  memory
#it follows a syntax similar to a python dictionary



#second method:(on_click)
import streamlit as st

st.title("Session State")
st.header("counter")

def add_one():
    st.session_state.counter+=1

if "counter" not in st.session_state:
    st.session_state["counter"] = 0

count = st.session_state.counter

# {
#     "counter" : 1
# }

st.button("Add one",on_click=add_one())


# if incremet:= st.button("Add 1"):
#     count+=1
#     st.session_state.counter = count
st.write(count)


#after refreshing memory will be cleared