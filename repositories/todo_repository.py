from google.cloud import firestore
from google.cloud.firestore_v1.base_query import FieldFilter, And
from pydantic import BaseModel
from typing import Dict
import os
from datetime import datetime

from dotenv import load_dotenv
    
load_dotenv()

SA_FILE_PATH = os.getenv("SA_FILE_PATH")

# Initialize Firestore client for database operations
firestore_db = firestore.Client.from_service_account_json(SA_FILE_PATH)

class TodoCreate(BaseModel):
    title: str
    priority: str = "Low"
    time_created: datetime = datetime.today().strftime("%d/%m/%Y, %H:%M:%S")
    completed: bool = False

class Todo(TodoCreate):
    todo_id: int

class User(BaseModel):
    username: str

class TodoRepository:
    def __init__(self):
        firestore_db.collection("Todo")

    def create_todo(self, todo: TodoCreate) -> Todo:
        new_todo = Todo(todo_id=len(self.todos) + 1, **todo.model_dump())
        todo_ref = firestore_db.collection("Todo").document()
        todo_ref.set({
            "user_id": "",
            "todo_id": new_todo.id,
            "title": new_todo.title,
            "completed": new_todo.title,
            "time_created": new_todo.time_created,
            "priority": new_todo.priority
        })
        return new_todo

    def get_todos(self) -> list[Todo]:
        todos = firestore_db.collection("Todo").where(filter=FieldFilter("user_id", "==", "")).stream()
        payload = []
        for todo in todos:
            payload.append(
                Todo(
                    user_id = todo.get("user_id"),
                    todo_id = todo.get("id"),
                    title = todo.get("title"),
                    completed = todo.get("completed"),
                    time_created = todo.get("time_created"),
                    priority = todo.get("priority")
                )
            )
        return payload

    def get_todo(self, todo_id: int) -> Todo | None:
        todo, *_ = firestore_db.collection("Todo").where(filter=FieldFilter("todo_id", "==", todo_id)).get()
        if todo.exists:
            return_val = Todo(
                user_id = todo.get("user_id"),
                todo_id = todo.get("id"),
                title = todo.get("title"),
                completed = todo.get("completed"),
                time_created = todo.get("time_created"),
                priority = todo.get("priority")
            )
            return return_val
        else:
            return None

    def update_todo(self, todo_id: int, updated_todo: TodoCreate) -> Todo | None:
        todo, *_ = firestore_db.collection("Todo").where(filter=FieldFilter("todo_id", "==", todo_id)).get()
        if todo.exists:
            todo.reference.update(dict(
                title = updated_todo.title,
                completed = updated_todo.completed,
                time_created = updated_todo.time_created,
                priority = updated_todo.priority
            ))
            return Todo(
                user_id = todo.get("user_id"),
                todo_id = todo.get("id"),
                title = todo.get("title"),
                completed = todo.get("completed"),
                time_created = todo.get("time_created"),
                priority = todo.get("priority")
            )
        else:
            return None

    def delete_todo(self, todo_id: int) -> bool:
        try:
            todo, *_ = firestore_db.collection("Todo").where(filter=FieldFilter("todo_id", "==", todo_id)).get()
            if todo.exists:
                todo.reference.delete()
                return True
            else:
                return False
        except KeyError:
            return False