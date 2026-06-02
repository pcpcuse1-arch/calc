import streamlit as st
st.header("maths quiz")
score=0
q1=st.radio("Q1.2+3=",[5,6,8,9])
q2=st.radio("Q2.82-59",[23,24,21,25])
q3=st.radio("Q3.49/7",[6,7,8,9])
q4=st.radio("Q4.49*10",[490,590,390,456])
q5=st.radio("Q5.5^4",[5,25,125,625])
if st.button("submit"):
    if q1==5:
        score=score+1
    if q2==23:
        score=score+1
    if q3==7:
        score=score+1
    if q4==490:
        score=score+1
    if q5==625:
        score=score+1
st.write("your score is:", score)
if score==5:
    st.balloons()
    st.success("excellent!")
elif score<5 and score>=3:
    st.write("very good!")
elif score<3 and score>=1:
    st.write("need to improve!")
else:
    st.error("try again")