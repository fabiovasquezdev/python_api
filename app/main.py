from fastapi import FastAPI
from app.database.session import engine, Base
from app.routers import user

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Python API",
    description="API RESTful",
    version="1.0.0"
)

app.include_router(user.router)

@app.get("/")
def read_root():
    return {"Python API"} 