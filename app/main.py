from fastapi import FastAPI
from . import models, database
from .auth import router as auth_router

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="FastAPI JWT Demo")

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def root():
    return {"message": "Bienvenido a la API con JWT"}
