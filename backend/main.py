from fastapi import FastAPI

app = FastAPI(title="Food Preorder API")

@app.get("/")
def read_root():
    return {"message": "cервер работает"}

@app.get("/health")
def health_check():
    return {"status": "ok"}