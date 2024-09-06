from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from decouple import Config, RepositoryEnv
from routers import todo_router

# Get the right environment
environment = os.getenv("ENVIRONMENT", "development")
config = Config(RepositoryEnv(f".env.{environment}"))

app = FastAPI()
app.include_router(todo_router.router)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=[f'{config("ORIGINS")}'],
    allow_credentials=True,
    allow_methods=[f'{config("METHODS")}'],
    allow_headers=["*"],
)

# Main block to run the application using Uvicorn server
if __name__ == "__main__":
    import uvicorn

    HOST = config("HOST")
    PORT = config("PORT")
    uvicorn.run("main:app", port=int(PORT), host=HOST, reload=True)