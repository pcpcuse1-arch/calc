import streamlit as st
a=st.number_input("enter number 1")
b=st.number_input("enter number 2")
if st.button("click"):
    c = a + b
    st.write("add=", c)