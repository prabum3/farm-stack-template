from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.utils import connect_to_mongo,close_mongo_connection
from db.mongodb import db
from settings import config

app = FastAPI(title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
  await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
  await close_mongo_connection()


@app.get("/api/v1")
async def root():
  return {"content":"Hello from FastAPI!!"}
