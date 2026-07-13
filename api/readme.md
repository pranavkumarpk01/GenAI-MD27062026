markdown_content = """# FastAPI & MongoDB Cheat Sheet

A well-structured reference guide for setting up a FastAPI application and configuring a MongoDB database using Docker.

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

## 🐳 Setting Up MongoDB via Docker

Follow these sequential steps to get your MongoDB database up and running in an isolated container environment:

1. **Install Docker**: Download and install Docker Desktop or use your system's Command Line Interface (CLI) to set it up.
2. **Pull the Official Mongo Image**: Download the latest MongoDB image from Docker Hub.
   ```bash
   docker pull mongo