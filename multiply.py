import streamlit as st
a=st.number_input("enter number 1")
b=st.number_input("enter number 2")
if st.button("multiply"):
    c = a * b
    st.write("multiply =", c)