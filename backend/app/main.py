from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import users, items
from .internal import admin

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 포함
app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"]
)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI"}
