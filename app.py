import streamlit as st

#take user input\

st.title("take the input")

name= st.text_input("enter your name")



if st.button ("submit"):
  st.write(f"name is:{name}")
