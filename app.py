import streamlit as st

st.title("My Notes Website")

st.header("Chapter 1")
with open("chapter1.md", "r", encoding="utf-8") as f:
    st.markdown(f.read())
