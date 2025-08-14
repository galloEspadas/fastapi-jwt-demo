from fastapi import FastAPI,Depends
from .auth import router as auth_router
from .utils import get_current_user
from . import crud

app = FastAPI(title="FastAPI JWT con MongoDB")

# Registrar rutas
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API con JWT y MongoDB"}


@app.get("/protected")
async def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hola {current_user}, accediste a un endpoint protegido"}

@app.get("/users", tags=["Users"])
async def list_users(current_user: str = Depends(get_current_user)):
    usernames = await crud.get_all_usernames()
    return {"total": len(usernames), "users": usernames}