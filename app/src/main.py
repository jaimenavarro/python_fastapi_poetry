from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.src.sql_db import crud, models, schemas
from app.src.sql_db.database import SessionLocal, engine
from app.src.redis_db.redis import get_redis_value, set_redis_value

from app.src import config

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

print(config.DEBUG)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
        user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.get("/item-redis/{item_id}", response_model=schemas.Item)
def read_items(item_id: int):
    response = schemas.Item(**(get_redis_value(item_id)))
    if response is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return response


@app.put("/item-redis/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.Item):
    set_redis_value(item_id, item)
    return item
