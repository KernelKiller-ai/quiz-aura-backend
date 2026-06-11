from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users_db = {
    "anurag@gmail.com": "123456"
}

class UserAuth(BaseModel):
    email: str
    password: str

@app.get("/")
def home():
    return {"status": "Quiz Aura Production Backend Live", "database": "Connected"}

@app.post("/signup")
def signup(user: UserAuth):
    email_clean = user.email.strip().lower()
    if email_clean in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[email_clean] = user.password
    return {"message": "Signup successful"}

@app.post("/login")
def login(user: UserAuth):
    email_clean = user.email.strip().lower()
    if email_clean not in users_db or users_db[email_clean] != user.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful", "username": email_clean.split("@")[0]}
