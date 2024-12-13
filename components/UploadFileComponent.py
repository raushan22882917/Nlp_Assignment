import streamlit as st

def upload_file_component():
    uploaded_file = st.file_uploader("Upload a file", type=["pdf", "txt"])
    return uploaded_file
