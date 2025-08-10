from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Sportsbook MVP API",
    description="Backend API for the sportsbook MVP project",
    version="1.0.0"
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Sportsbook MVP backend is running"}

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
