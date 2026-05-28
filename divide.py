import streamlit as st
a=st.number_input("enter no 1")
b=st.number_input("enter number 2")
if st.button("divide"):
 c = a / b
 st.write("divide =", c)