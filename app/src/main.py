from fastapi import FastAPI
from app.src.api import users, admin


app = FastAPI()

app.include_router(users.router)
app.include_router(admin.router)
