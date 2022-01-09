from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.utils import connect_to_mongo,close_mongo_connection
from db.mongodb import db
import os
import random


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
  items["count"] = random.randint(0,10000)

@app.on_event("shutdown")
async def shutdown_event():
  await close_mongo_connection()


@app.get("/api")
async def root():
  database = db.client.stacks
  ccount = items["count"]
  document = {'pk': f"no{ccount}no",'new':'yes','count':ccount}
  items["count"]+=1
  result = await database.dummy.insert_one(document)
  return {"content":"Hello from FastAPI!!"}
