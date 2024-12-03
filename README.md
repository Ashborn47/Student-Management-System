# FastAPI Student Management API

A complete **FastAPI** application for managing student records, built with MongoDB as the database and Motor for asynchronous interaction.  

## Features

This project includes the following components:
- **`config.py`**: Configuration management using Pydantic settings.
- **`database.py`**: MongoDB connection setup with Motor.
- **`models.py`**: Pydantic models for data validation.
- **`main.py`**: The main FastAPI application containing all API endpoints.

### API Endpoints

| Method | Endpoint                      | Description                  |
|--------|-------------------------------|------------------------------|
| `GET`  | `/students`                  | List all students            |
| `GET`  | `/students/{student_id}`     | Retrieve a specific student  |
| `POST` | `/students`                  | Create a new student         |
| `PUT`  | `/students/{student_id}`     | Update an existing student   |
| `DELETE` | `/students/{student_id}`   | Delete a student             |

---

## Setup Instructions

### Prerequisites
1. Install [Python 3.10+](https://www.python.org/downloads/).
2. Create a **MongoDB Atlas** cluster or use your local MongoDB instance.
3. Clone this repository.

```bash
git clone https://github.com/your-username/fastapi-student-management.git
cd fastapi-student-management
