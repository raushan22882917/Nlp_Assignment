# Assignment 
### Instructions for Setup and Running

#### 1. Setting Up the Environment
Before running the application, make sure you have Python installed. Follow these steps to set up your environment:

1. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables** (optional, if specific configuration settings are needed):
   ```bash
   export GROQ_API_KEY='your_groq_api_key_here'
   ```

#### 2. Running the Frontend (Streamlit)
To run the Streamlit frontend:

```bash
streamlit run main.py
```

- This will start the Streamlit app and open it in your default web browser.

#### 3. Running the Backend (FastAPI)
To run the FastAPI backend locally:

```bash
uvicorn app.main:app --reload
```

- This command starts the FastAPI application, making it accessible locally at `http://127.0.0.1:8000`.
- You can access the API endpoints defined in `app/routes.py`.

#### 4. Deploying the Application
To deploy the application, you need to:

1. **Deploy the FastAPI backend** on a service like Render, Heroku, or AWS:
   - For example, if using Render:
     ```bash
     render deploy
     ```
   - You can then test your deployment by visiting the provided URL (e.g., https://nlp-assignment-y2ca.onrender.com/).

#### 5. Video Demonstration
You can view a video demonstration of the application here:
- [Video Link](https://drive.google.com/file/d/1Sp44M_n9_XnpXIdufGOnULEW4jYBAwSn/view?usp=sharing)

#### 6. API Endpoints
Your FastAPI app should include the following routes in `app/routes.py`:

- `/upload`: For uploading files.
- `/process`: To extract content from uploaded files.
- `/query`: To process queries based on the extracted content.
- `/visualize`: To display results in a graphical form.

#### Example Queries
For testing, you can use these queries:
1. **"Summarize the report's financial section."**
2. **"Extract the revenue distribution across Electronics, Clothing, and Home Essentials."**
3. **"Identify the impact of supply chain costs on the Electronics division's profit margins."**
4. **"Provide details of the two proposals to address supply chain issues in Electronics."**
5. **"Analyze the effect of marketing budget allocation on the Clothing division's sales growth."**

This setup and structure will allow users to upload files, extract content, query the document, and visualize the results, all while maintaining clear instructions for local and deployed use. 

