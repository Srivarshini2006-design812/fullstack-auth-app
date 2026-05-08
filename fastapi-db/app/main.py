from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

# -------------------------
# CORS
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://fullstack-auth-app-swart.vercel.app",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# DATABASE
# -------------------------
def get_conn():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

# -------------------------
# MODELS
# -------------------------
class User(BaseModel):
    name: str
    password: str

class Todo(BaseModel):
    text: str

# -------------------------
# HOME
# -------------------------
@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

# -------------------------
# REGISTER
# -------------------------
@app.post("/register")
def register(user: User):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT,
            password TEXT
        )
    """)

    cur.execute(
        "INSERT INTO users (name, password) VALUES (%s, %s)",
        (user.name, user.password)
    )

    conn.commit()

    cur.close()
    conn.close()

    return {"message": "User registered successfully"}

# -------------------------
# LOGIN
# -------------------------
@app.post("/login")
def login(user: User):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE name=%s AND password=%s",
        (user.name, user.password)
    )

    existing_user = cur.fetchone()

    cur.close()
    conn.close()

    if existing_user:
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid username or password"}

# -------------------------
# GET USERS
# -------------------------
@app.get("/users")
def get_users():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM users")

    users = cur.fetchall()

    cur.close()
    conn.close()

    return {"users": users}

# -------------------------
# CREATE TODO
# -------------------------
@app.post("/todos")
def create_todo(todo: Todo):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id SERIAL PRIMARY KEY,
            text TEXT
        )
    """)

    cur.execute(
        "INSERT INTO todos (text) VALUES (%s)",
        (todo.text,)
    )

    conn.commit()

    cur.close()
    conn.close()

    return {"message": "Todo created"}

# -------------------------
# GET TODOS
# -------------------------
@app.get("/todos")
def get_todos():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT * FROM todos")

    todos = cur.fetchall()

    cur.close()
    conn.close()

    return {"todos": todos}
