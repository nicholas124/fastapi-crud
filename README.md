# FastAPI CRUD

This is a FastAPI project implementing CRUD (Create, Read, Update, Delete) operations. The project follows a structured layout for better organization and scalability.

## Project Structure

fastapi-crud
├── docker-compose.yml
└── src
    ├── Dockerfile
    ├── app
    │   ├── __init__.py
    │   ├── api
    │   │   ├── __init__.py
    │   │   ├── crud.py
    │   │   ├── models.py
    │   │   ├── notes.py
    │   │   └── ping.py
    │   ├── db.py
    │   └── main.py
    ├── requirements.txt
    └── tests
        ├── __init__.py
        ├── conftest.py
        ├── test_notes.py
        └── test_ping.py


## Components

- **docker-compose.yml**: Docker Compose configuration file for orchestrating containers.

- **Dockerfile**: Docker configuration file for building the project image.

- **src/app**: Application source code directory.

    - **api**: API endpoints and related modules.

        - **crud.py**: CRUD operations for the application.

        - **models.py**: Data models for the application.

        - **notes.py**: Implementation of the notes API.

        - **ping.py**: Implementation of the ping API.

    - **db.py**: Database configuration and setup.

    - **main.py**: Main FastAPI application entry point.

- **requirements.txt**: List of Python dependencies required for the project.

- **tests**: Directory containing unit tests for the application.

    - **test_notes.py**: Unit tests for the notes API.

    - **test_ping.py**: Unit tests for the ping API.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/fastapi-crud.git
docker-compose up --build
