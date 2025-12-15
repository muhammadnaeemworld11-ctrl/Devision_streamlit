import streamlit as st 
st.title("SIMPLE DEVISION CALCULATOR ")

num1 = st.number_input("Enter first number to devide: ")
num2 = st.number_input("Enter second number to devide: ")
if num1 == 0 or num2 == 0:
    st.error("Zero devision Error")
else:
    st.success(num1 / num2)
