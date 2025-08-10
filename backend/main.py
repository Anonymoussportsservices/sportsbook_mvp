from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Sportsbook MVP API",
    description="Backend API for the sportsbook MVP project",
    version="1.0.0"
)

origins = [
    origins = [
    "http://localhost:3000",
    "https://sportsbook-mvp2-0.onrender.com/",
]

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
