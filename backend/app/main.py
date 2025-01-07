from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from .schemas.graphql import schema  # GraphQL 스키마 임포트
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

# GraphQL 라우터 추가
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# 기존 REST API 라우터들
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