from fastapi import APIRouter, Depends
from app.deps import get_current_user
from app.db import get_conn

router = APIRouter()

# CREATE TODO
@router.post("/todos")
def create_todo(title: str, user=Depends(get_current_user)):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO todos (title, user_id) VALUES (%s, %s)",
        (title, user["user_id"])
    )

    conn.commit()

    cur.close()
    conn.close()

    return {"message": "Todo created"}

# GET TODOS
@router.get("/todos")
def get_todos(user=Depends(get_current_user)):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, title FROM todos WHERE user_id = %s",
        (user["user_id"],)
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return {
        "todos": [
            {"id": r[0], "title": r[1]}
            for r in rows
        ]
    }
