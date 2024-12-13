import streamlit as st

def query_component():
    query = st.text_input("Enter your query")
    return query
