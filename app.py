import streamlit as st

#take user input\
name= st.text_input("enter your name")
st.title("take the input")

if st.button ("submit"):
  st.write(f"name is:{name}")
