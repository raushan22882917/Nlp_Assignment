import streamlit as st
from utils import upload_file, query_groq_api_with_groq_lib


# Set page configuration
st.set_page_config(page_title="Document Analysis System", layout="wide")

st.title("Document Analysis System")

# File uploader to upload either PDF or text file
uploaded_file = st.file_uploader("Upload a PDF or Text File", type=["pdf", "txt"])

if uploaded_file is not None:
    # Displaying uploaded file details
    st.write(f"Uploaded file: {uploaded_file.name}")

    # Upload the file and extract content
    file_content, content_id = upload_file(uploaded_file)

    # Ask for user query
    query = st.text_input("Enter your query related to the document")

    if st.button("Submit Query"):
        if query:
            # Pass the extracted content and user query to GroQ API for an answer
            query_response = query_groq_api_with_groq_lib(query, file_content)
            
            # Display query results
            st.subheader("Query Results:")
            st.json(query_response)

            # Display short summary from the response
            if "summary" in query_response["response"]:
                st.subheader("Document Summary:")
                st.write(query_response["response"]["summary"])

            # Display the key points with integer percentages for revenue changes
            if "key_points" in query_response["response"]:
                st.subheader("Key Points:")
                for point, value in query_response["response"]["key_points"].items():
                    st.write(f"{point}: {value}")
        else:
            st.error("Please enter a query.")
else:
    st.info("Please upload a file to get started.")
