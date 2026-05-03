from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Postgres Task Manager")


@app.get(
    "/tasks",
    response_model=List[schemas.TaskResponse],
    tags=["Tasks"],
    summary="Get a list of all tasks",
    description="Returns a list of all tasks with the ability to filter by completion status."
)
def read_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()


@app.post(
    "/tasks",
    response_model=schemas.TaskResponse,
    status_code=200,
    tags=["Tasks"],
    summary="Create a new task"
)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.patch(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse,
    tags=["Tasks"],
    summary="Update data of a task",
    description="Allows you to partially change status of a task."
)
def update_task_status(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.is_completed = not db_task.is_completed
    db.commit()
    db.refresh(db_task)
    return db_task


@app.delete(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse,
    status_code=200,
    tags=["Tasks"],
    summary="Delete task and return it's data"
)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    task_data = schemas.TaskResponse.model_validate(db_task)

    db.delete(db_task)
    db.commit()

    return task_data
