from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sportsbook-mvp.onrender.com"],  # your frontend URL here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API is working"}


@app.get("/api/users")
async def get_users():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

@app.post("/api/users")
async def create_user(user: User):
    # For now, just return the user data back
    return user

@console.log("About to call API");
fetch("https://sportsbook-mvp2-0.onrender.com/api/endpoint")
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));
