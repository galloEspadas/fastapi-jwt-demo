from fastapi import APIRouter, HTTPException, status
from . import schemas, crud, utils, config

router = APIRouter()

@router.post("/register", response_model=schemas.Token)
async def register(user: schemas.UserCreate):
    existing = await crud.get_user_by_username(user.username)
    if existing:
        raise HTTPException(status_code=400, detail="Usuario ya existe")

    await crud.create_user(user.username, user.password)
    token = utils.create_access_token({"sub": user.username}, config.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {"Usuario registrtado correctamente"}

@router.post("/login", response_model=schemas.Token)
async def login(user: schemas.UserLogin):
    db_user = await crud.get_user_by_username(user.username)
    if not db_user or not utils.verify_password(user.password, db_user["password_hash"]):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = utils.create_access_token({"sub": user.username}, config.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {"access_token": token, "token_type": "bearer"}
