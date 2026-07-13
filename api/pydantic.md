<!-- # FastAPI & MongoDB Cheat Sheet

A well-structured reference guide for setting up a FastAPI application, configuring a MongoDB database using Docker, and implementing Pydantic data validation.

---

## 🚀 Core Web Framework & Server

*   **FastAPI**: The core Python framework used to build your application and web APIs.
*   **Uvicorn**: The ASGI server that runs your FastAPI application at a desired port. It also exposes the built-in **Swagger UI** (interactive documentation) to visually test your APIs.
*   **Dependency Management**: 
    ```bash
    pip install -r requirements.txt
    ```
    Use this command to quickly install all required libraries listed in your project.

---

## 🛡️ Data Validation with Pydantic

Pydantic helps you validate that the incoming data from a client matches your expected format. If the client sends invalid data, **the request never reaches your endpoint function**, preventing bad data from hitting your logic or database.

### 1. The Problem: Without Pydantic
When using a generic `dict`, FastAPI accepts any payload shape or data type, which can lead to malformed records in your database.

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/students")
def create_student(student: dict):
    # DANGER: Accepts invalid types (e.g., strings for age, integers for city)
    collection.insert_one(student)
    return {"message": "created"} -->