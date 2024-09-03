from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import google.oauth2.id_token
from google.auth.transport import requests
from google.cloud import firestore
from google.cloud.firestore_v1.base_query import FieldFilter, And
from firebase_admin import credentials
import firebase_admin

from dotenv import load_dotenv

from routers import todo_router

app = FastAPI()
app.include_router(todo_router.router)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Firestore client for database operations
firestore_db = firestore.Client.from_service_account_json('firebase_iam.json')

# Set up request adapter for Firebase authentication
firebase_request_adapter = requests.Request()

# initialize the service account
credentials = credentials.Certificate('firebase_iam.json')
firebase_admin.initialize_app(credentials)

# Main block to run the application using Uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)