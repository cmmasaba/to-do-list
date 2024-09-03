from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

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

# Main block to run the application using Uvicorn server
if __name__ == "__main__":
    import uvicorn
    from dotenv import load_dotenv

    load_dotenv()

    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    uvicorn.run("main:app", port=PORT, host=HOST, reload=True)