from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os

app = FastAPI()

# ✅ CORS FIX (CRITICAL FOR VERCEL + RENDER)
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

# ✅ DB CONNECTION (CLOUD SAFE)
def get_conn():
    return psycopg2.connect(os.getenv("DATABASE_URL"))


@app.get("/")
def home():
    return {"message": "Backend running 🚀"}


# -------------------------
# REGISTER (example fix)
# -------------------------
@app.post("/register")
def register():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT 1")  # replace with real insert later
    conn.commit()

    cur.close()
    conn.close()

    return {"message": "Register success"}


# -------------------------
# LOGIN (example fix)
# -------------------------
@app.post("/login")
def login():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT 1")  # replace with real auth later
    conn.commit()

    cur.close()
    conn.close()

    return {"message": "Login success"}
