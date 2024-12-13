import streamlit as st

def results_component(summary, key_points):
    st.write(summary)
    st.write("Key Points:")
    for key, value in key_points.items():
        st.write(f"{key}: {value}")
