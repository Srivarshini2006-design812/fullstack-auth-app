from app.db import get_conn
from app.auth import hash_password, verify_password, create_token

# ---------------- REGISTER ----------------
def create_user(name: str, password: str):
    conn = get_conn()
    cur = conn.cursor()

    hashed = hash_password(password)

    cur.execute(
        "INSERT INTO users (name, password) VALUES (%s, %s)",
        (name, hashed)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"status": "created", "name": name}

# ---------------- LOGIN ----------------
def login_user(name: str, password: str):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE name=%s", (name,))
    user = cur.fetchone()

    cur.close()
    conn.close()

    if not user:
        return None

    user_id, hashed = user

    if not verify_password(password, hashed):
        return None

    return create_token({"user_id": user_id})
