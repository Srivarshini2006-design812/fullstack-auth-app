from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.users import router as users_router
from app.routers.todos import router as todos_router

from app.init_db import init_db

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# STARTUP
@app.on_event("startup")
def startup():
    init_db()

# ROUTES
app.include_router(users_router)
app.include_router(todos_router)

# HEALTH
@app.get("/health")
def health():
    return {"status": "ok"}
