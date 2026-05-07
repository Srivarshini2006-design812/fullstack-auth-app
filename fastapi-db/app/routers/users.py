from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate
from app.services.user_service import create_user, login_user
from app.deps import get_current_user
from app.db import get_conn

router = APIRouter()

# ---------------- REGISTER ----------------
@router.post("/register")
def register(user: UserCreate):
    return create_user(user.name, user.password)

# ---------------- LOGIN ----------------
@router.post("/login")
def login(name: str, password: str):
    token = login_user(name, password)
    if not token:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": token}

# ---------------- USERS (PROTECTED) ----------------
@router.get("/users")
def get_users(user=Depends(get_current_user)):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM users")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return {"users": [{"id": r[0], "name": r[1]} for r in rows]}
