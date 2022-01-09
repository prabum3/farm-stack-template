from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.utils import connect_to_mongo,close_mongo_connection
from db.mongodb import db
import os


app = FastAPI()
items = {}

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
  items.count = 0

@app.on_event("shutdown")
async def shutdown_event():
  await close_mongo_connection()


@app.get("/api")
async def root():
  database = db.client.stacks
  document = {'pk': 'nothine','new':'yes','count':items.count}
  items.count+=1
  result = await database.dummy.insert_one(document)
  print(result)
  envValue = os.getenv("mongodb","notfound")
  return {"content":f"Hello from FastAPI!! {envValue}"}
