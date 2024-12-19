from fastapi import FastAPI
from app.routers import task_router, user_router

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to Taskmanager"}

# Подключаем маршруты
app.include_router(task_router)
app.include_router(user_router)