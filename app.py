import streamlit as st
a=st.number_input("enter number 1")
b=st.number_input("enter number 2")
if st.button("add"):
    c = a + b
    st.write("add=", c)
if st.button("sub"):
    c = a - b
    st.write("subtract =", c)       
if st.button("mul"):
    c = a * b
    st.write("multiply =", c)       
if st.button("/"):
    c = a / b
    st.write("divide =", c) 
