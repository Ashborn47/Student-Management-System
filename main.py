from fastapi import FastAPI
from routes import student_routes

app = FastAPI(title="Student Management System")

# Include routers
app.include_router(student_routes.router, tags=["students"])