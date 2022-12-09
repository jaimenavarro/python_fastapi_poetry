from fastapi import FastAPI
from app.src.api import users, admin

from app.src.sql_db import models
from app.src.sql_db.connection import engine

# Create all tables stored in this metadata.
models.Base.metadata.create_all(bind=engine)

# Creates an application instance.
app = FastAPI()

# Add routes to the application
app.include_router(users.router)
app.include_router(admin.router)
