from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import firebase_admin
from firebase_admin import credentials, auth
import os
from dotenv import load_dotenv
    
load_dotenv()

SA_FILE_PATH = os.getenv("SA_FILE_PATH")

# initialize the service account
cred = credentials.Certificate(SA_FILE_PATH)
firebase_admin.initialize_app(cred)

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )