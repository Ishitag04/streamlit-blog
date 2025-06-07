import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

# print(plt.style.available) -> prints all the styles available in matplotlib

# plt.style.use("ggplot")

data = {
    "num" : [x for x in range(1,11)],
    "square" : [x**2 for x in range(1,11)],
    "twice" : [x*2 for x in range(1,11)],
    "thrice" : [x*3 for x in range(1,11)]
}


rad = st.sidebar.radio("Navigation",["Home","About Us","Others"])

if rad=="Home":
    df = pd.DataFrame(data)
    # print(df)

    # st.sidebar.selectbox("Select a number",[1,2,3,4,5])
    col = st.sidebar.selectbox("Select a column",df.columns)

    plt.plot(df['num'],df[col])
    st.pyplot()

    # col2 = st.sidebar.multiselect("Select a column",df.columns)

    # plt.plot(df['num'],df[col2])
    # st.pyplot()

if rad=="About Us":
    st.write("You are here in about us page")

    #Status messages (5)
    st.error("Error")
    st.success("Show success")
    st.info("Information")
    st.exception(RuntimeError("this is an error"))
    st.warning("This is a warning")


if rad=="Others":
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)

    st.balloons()





# def points():
#     xs = st.sidebar.text_input("Enter the point between which you want to see the graph, x = ")

#     ys = st.sidebar.text_input("Enter the point between which you want to see the graph, y = ")

#     plt.scatter(xs,ys)
#     st.pyplot()

# points()







# if st.sidebar.checkbox("Do you want to add more point?"):
#     points()
#     # a = st.sidebar.text_input("Enter the point between which you want to see the graph, x = ")
#     # xs.append(a)

#     # b = st.sidebar.text_input("Enter the point between which you want to see the graph, y = ")
#     # ys.append(b)

#     # plt.scatter(xs,ys)
#     # st.pyplot()