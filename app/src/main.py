from fastapi import FastAPI

from app.src.api import users, admin, actuators
from app.src.sql_db import models
from app.src.sql_db.connection import engine
from app.src.redis_db.redis import db_redis

# Create all tables stored in this metadata.
models.Base.metadata.create_all(bind=engine)

# Creates an application instance.
app_name = "FastAPI App with Pyctuator"
app = FastAPI(title=app_name)

# Add routes to the application
app.include_router(users.router)
app.include_router(admin.router)

# Load and configure actuator
actuator_api = actuators.ActuatorAPI(app)
actuator_api.register_sql_db_health_provider(engine)
actuator_api.register_redis_db_health_provider(db_redis)


