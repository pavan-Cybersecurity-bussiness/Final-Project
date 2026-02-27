# Final-Project
This is the final project using fastapi for B1 Programming

Project Overview

This project is a complete FastAPI backend application that manages tasks through a RESTful API.
All task data is stored in a plain text file using JSON Lines format for persistence across server restarts.

Each line in tasks.txt represents one task as a JSON object.

Features

Create tasks

Retrieve all tasks

Retrieve a single task by ID

Update tasks

Delete a single task

Delete all tasks

Filter tasks by completion status

Get task statistics (total, completed, pending, percentage)

Data Storage Method

Tasks are stored in tasks.txt using JSON Lines format:

Example:

{"id":1,"title":"Learn FastAPI","description":"Watch tutorial","completed":false}
{"id":2,"title":"Buy groceries","description":"Milk","completed":true}

This ensures:

Persistence across server restarts

Simple file-based backend logic

Understanding of fundamental data storage concepts

Project Structure
fastapi-tasks/
│── main.py
│── models.py
│── file_handler.py
│── tasks.txt
│── README.md
Setup Instructions

Install dependencies:

pip install fastapi uvicorn

Create an empty tasks.txt file.

Run the server:

uvicorn main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs
API Endpoints
Method	Endpoint	Description
GET	/	Root check
GET	/tasks	Get all tasks
GET	/tasks?completed=true	Filter tasks
GET	/tasks/{id}	Get single task
POST	/tasks	Create task
PUT	/tasks/{id}	Update task
DELETE	/tasks/{id}	Delete single task
DELETE	/tasks	Delete all tasks
GET	/tasks/stats	Task statistics
Data Model
id: int (auto-generated, sequential)
title: str (required)
description: str (optional)
completed: bool (default: false)
Persistence Guarantee

Tasks are stored in a text file and written to disk after every modification, ensuring data remains available even after server restarts.
