from typing import Annotated

import models
import schemas
from database import engine, get_db
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# Create tables
models.Base.metadata.create_all(bind=engine)

# Create app
app = FastAPI()

# Database section dependency
CurrentSession = Annotated[Session, Depends(get_db)]


@app.post('/items/', response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: CurrentSession):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get('/items/', response_model=list[schemas.Item])
def get_items(db: CurrentSession, skip: int = 0, limit: int = 10):
    return db.query(models.Item).offset(skip).limit(limit).all()


@app.get('/items/{item_id}', response_model=schemas.Item)
def get_item(item_id: int, db: CurrentSession):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()

    if not db_item:
        raise HTTPException(status_code=404, detail='Item not found.')

    return db_item


@app.put('/items/{item_id}', response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemCreate, db: CurrentSession):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()

    if not db_item:
        raise HTTPException(status_code=404, detail='Item not found.')

    for key, value in item.model_dump().items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item


@app.delete('/item/{item_id}', response_model=schemas.Item)
def delete_item(item_id: int, db: CurrentSession):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()

    if not db_item:
        raise HTTPException(status_code=404, detail='Item not found.')

    db.delete(db_item)
    db.commit()
    return db_item
