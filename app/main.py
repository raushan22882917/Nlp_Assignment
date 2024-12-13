from fastapi import FastAPI
from app.routes import router  # import the router you defined earlier

app = FastAPI()

# Include the router that contains your routes
app.include_router(router)
