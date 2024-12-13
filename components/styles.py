# styles.py
# CSS-like styles for Streamlit UI customization
STYLES = """
    <style>
    .stTextInput input {
        width: 100%;
    }
    </style>
"""

def apply_styles():
    st.markdown(STYLES, unsafe_allow_html=True)
