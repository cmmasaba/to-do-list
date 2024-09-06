# Todo List
A simple python REST API service illustrating how to do modularization in FastAPI applications. Modularization is the concept of separating concerns in an application i.e. routing, business logic, data storage, and authentication are handled separately as different layers/services.<br>

## Stack
- Language: Python 3.10+
- Framework: FastAPI
- Authentication: Firebase
- Storage: Firestore NoSQL

## API
- POST /todos: create a new todo item
- GET /todos: get all todo items for the given user
- GET /todos/{todo_id}: get a todo item with the given id
- PUT /todos/{todo_id}: update a todo item with the given id
- DELETE /todos/{todo_id}: delete a todo item with the given id

## APP MODULES
- **Auth**: handles the authentication of users when they access the API.
- **Controllers**: handles incoming requests, orchestrates the API logic and manages the flow of data between API routes and services layer.
- **Repositories**: provides a standardized set of methods for storing, retrieving, updating and deleting data. This provides an abstraction for data persistence. operations, encapsulating interactions with the database and external data sources.
- **Routers**: group all relaed API endpoints into one file
- **Services**: contains the businesss of the API and implements specific functionalities and operations required by the application.

## License and Copyright
See the MIT license attached for terms of use.<br>
&copy; 2024 Collins Mmasaba