from fastapi import FastAPI
from auth import router as auth_router

app = FastAPI(title="Food Preorder API")

app.include_router(auth_router, prefix="/auth", tags=["Авторизация"])

@app.get("/")
def read_root():
    return {"message": "Сервер работает! 🍕"}

@app.get("/health")
def health_check():
    return {"status": "ok"}