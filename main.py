from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    name: str = Field(..., min_length=1)
    age: int = Field(..., gt=0)

@app.post("/greet")
def greet_user(user: User):
    return {"message": f"Hello, {user.name} ({user.age})!"}
