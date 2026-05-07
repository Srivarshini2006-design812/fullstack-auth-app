
import os
from passlib.context import CryptContext
from jose import jwt
import datetime
from dotenv import load_dotenv

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

# ---------------- PASSWORD ----------------
def hash_password(password: str):
    return pwd_context.hash(password[:72])

def verify_password(plain, hashed):
    return pwd_context.verify(plain[:72], hashed)

# ---------------- TOKEN ----------------
def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
