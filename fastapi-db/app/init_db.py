from app.db import get_conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    # USERS TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # TODOS TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        user_id INTEGER REFERENCES users(id)
    )
    """)

    conn.commit()

    cur.close()
    conn.close()
