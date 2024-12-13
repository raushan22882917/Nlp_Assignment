import uuid
import pdfplumber
from typing import Tuple
from io import BytesIO
from groq import Groq
import os
import re

# Assuming your GroQ API credentials and endpoint are stored in environment variables or config
GROQ_API_KEY = "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"
GROQ_API_URL = "https://groqapi.com/endpoint"

# Initialize GroQ client
client = Groq(api_key=GROQ_API_KEY)

# Upload file and extract content (supports PDF and text files)
def upload_file(file: BytesIO) -> Tuple[str, str]:
    """
    Uploads a file and extracts its content. Supports PDF and text files.
    Args:
        file (BytesIO): The file to be uploaded.
    Returns:
        Tuple[str, str]: Extracted content and a unique content ID.
    """
    content_id = str(uuid.uuid4())  # Unique ID for the uploaded content
    content = ""
    
    # Check if PDF
    try:
        with pdfplumber.open(file) as pdf:
            content = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
        if content:
            return content, content_id
    except Exception:
        pass
    
    # Check if it's a text file
    file.seek(0)
    content = file.read().decode("utf-8")
    
    return content, content_id

# Function to query GroQ API and structure the response as JSON
def query_groq_api_with_groq_lib(query: str, file_content: str) -> dict:
    """
    Queries the GroQ API with a query and document content.
    Args:
        query (str): The user's query.
        file_content (str): Extracted content from the uploaded document.
    Returns:
        dict: A structured response including the query result and summary.
    """
    # Send the query to the GroQ chat API using the 'groq' library
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"Given the document content, please respond to the query: {query}. Extract the relevant data from the provided content to answer the query."
            },
            {"role": "assistant", "content": file_content},  # Pass the document content here
            {
                "role": "user",
                "content": "Now, provide a short summary of the entire document content."
            }
        ],
        model="llama3-8b-8192",
    )
    
    response_content = chat_completion.choices[0].message.content

    # Structure the response into the desired format
    structured_response = {
        "query": query,
        "response": {
            "summary": response_content,  # The short summary provided by the API
            "key_points": extract_key_points(response_content)  # Function to extract key points from the response
        }
    }

    return structured_response

# Function to extract key points from the response (this is a placeholder, and can be customized further)
def extract_key_points(response_content: str) -> dict:
    """
    Extracts key points from the response content.
    Args:
        response_content (str): The response content from the GroQ API.
    Returns:
        dict: A dictionary of key points.
    """
    key_points = {}

    # Find percentage patterns using regex with surrounding words
    matches = re.finditer(r"(\b\w+\s+\w+\s+\w+\b).*?(\d+)%", response_content)
    for match in matches:
        key_words = match.group(1).lower().split()  # Split into words and lower case them
        percentage = int(match.group(2))  # The percentage itself
        
        # Check if 'revenue' or 'income' is among the words before the percentage
        if any(word in key_words for word in ['revenue', 'income']):
            key_points[match.group(1)] = f"{percentage}%"
    
    # Example: Looking for specific terms in the response content
    if "revenue increased by" in response_content.lower():
        key_points["revenue"] = "Increase/Decrease in revenue"
    
    if "income" in response_content.lower():
        key_points["net_income"] = "Increase/Decrease in net income"
    
    return key_points