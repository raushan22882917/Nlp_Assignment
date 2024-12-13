from fastapi import FastAPI

app = FastAPI()

# Include routes
from . import routes
