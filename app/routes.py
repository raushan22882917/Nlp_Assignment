from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from .utils import upload_file, query_groq_api

router = APIRouter()

# Upload endpoint
@router.post("/upload")
async def upload_file_route(file: UploadFile = File(...)):
    try:
        # Process the uploaded file
        file_content, content_id = upload_file(file.file)
        
        # Return response with content and content_id
        return JSONResponse(content={"content_id": content_id, "content": file_content})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Query endpoint
@router.post("/query")
async def query_groq_api_route(query: str, content_id: str):
    try:
        # Query the extracted content using GroQ API
        response = query_groq_api(query, content_id)
        
        # Return the response from GroQ API
        return JSONResponse(content=response)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
