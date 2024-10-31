from fastapi import FastAPI
from src.routing.refer.referal import referal_router
from src.routing.user.user import users_router
from src.routing.auth.auth import auth_router

app = FastAPI()

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(referal_router)
