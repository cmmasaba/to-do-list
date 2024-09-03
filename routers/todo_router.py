from fastapi import APIRouter, Depends
from controllers.todo_controller import TodoController, TodoCreate, Todo
from auth.todo_auth import verify_token

router = APIRouter()
todo_controller = TodoController()

@router.post("/auth/verify-token")
async def verify_token_endpoint(decoded_token: dict = Depends(verify_token)):
    return {"status": "success", "user_id": decoded_token['uid']}

@router.post("/todos", response_model=Todo, dependencies=[Depends(verify_token)])
async def create_todo(todo: TodoCreate):
    return todo_controller.create_todo(todo)

@router.get("/todos", response_model=list[Todo], dependencies=[Depends(verify_token)])
async def get_todo():
    return todo_controller.get_todos()

@router.get("/todos/{todo_id}", response_model=Todo, dependencies=[Depends(verify_token)])
async def get_todo(todo_id: int):
    return todo_controller.get_todo(todo_id)

@router.put("/todos/{todo_id}", response_model=Todo, dependencies=[Depends(verify_token)])
async def update_todo(todo_id: int, updated_todo: TodoCreate):
    return todo_controller.update_todo(todo_id, updated_todo)

@router.delete("/todos/{todo_id}", dependencies=[Depends(verify_token)])
async def delete_todo(todo_id: int):
    todo_controller.delete_todo(todo_id)