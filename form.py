import streamlit as st
st.header("registeration form")
name=st.text_input("enter your name")
email=st.text_input("enter your email")
password=st.text_input("enter your password")
age=st.number_input("enter your age")
st.button("submit")