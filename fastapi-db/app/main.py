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
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# DATABASE CONNECTION
# -------------------------
def get_conn():
    return psycopg2.connect(os.getenv("DATABASE_URL"))


# -------------------------
# USER MODEL
# -------------------------
class User(BaseModel):
    name: str
    password: str


# -------------------------
# TODO MODEL
# -------------------------
class Todo(BaseModel):
    task: str


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
    try:
        conn = get_conn()
        cur = conn.cursor()

        # create users table if not exists
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT,
                password TEXT
            )
        """)

        conn.commit()

        # insert user
        cur.execute(
            "INSERT INTO users (name, password) VALUES (%s, %s)",
            (user.name, user.password)
        )

        conn.commit()

        cur.close()
        conn.close()

        return {"message": "User registered successfully"}

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# LOGIN
# -------------------------
@app.post("/login")
def login(user: User):
    try:
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

        return {"message": "Invalid credentials"}

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# GET USERS
# -------------------------
@app.get("/users")
def get_users():
    try:
        conn = get_conn()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT,
                password TEXT
            )
        """)

        conn.commit()

        cur.execute("SELECT id, name FROM users")

        users = cur.fetchall()

        cur.close()
        conn.close()

        return {
            "users": [
                {"id": user[0], "name": user[1]}
                for user in users
            ]
        }

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# CREATE TODO
# -------------------------
@app.post("/todos")
def create_todo(todo: Todo):
    try:
        conn = get_conn()
        cur = conn.cursor()

        # create todos table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id SERIAL PRIMARY KEY,
                task TEXT
            )
        """)

        conn.commit()

        # insert todo
        cur.execute(
            "INSERT INTO todos (task) VALUES (%s)",
            (todo.task,)
        )

        conn.commit()

        cur.close()
        conn.close()

        return {"message": "Todo created successfully"}

    except Exception as e:
        return {"error": str(e)}


# -------------------------
# GET TODOS
# -------------------------
@app.get("/todos")
def get_todos():
    try:
        conn = get_conn()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id SERIAL PRIMARY KEY,
                task TEXT
            )
        """)

        conn.commit()

        cur.execute("SELECT * FROM todos")

        todos = cur.fetchall()

        cur.close()
        conn.close()

        return {
            "todos": [
                {"id": todo[0], "task": todo[1]}
                for todo in todos
            ]
        }

    except Exception as e:
        return {"error": str(e)}
