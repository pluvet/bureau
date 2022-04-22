import ast
import json
import os

from fastapi import APIRouter
import asyncio
from httpx import AsyncClient
from config.db import conn
from models.bureau import Bureau
from schemas.bureau import serializeDict, serializeList
from motor import motor_asyncio
from pydantic import BaseModel
from pymongo import DESCENDING

bureau = APIRouter()




@bureau.get('/')
async def find_all():
  #  print(conn.local.user.find())
  #  print(serializeList(conn.local.user.find()))
    data = conn.local.check.find().sort([('_id', DESCENDING)])
    data = await data.to_list(None)
    #print(type(data))
  
    #print (data)

    return serializeList(data)

@bureau.post('/')
async def create_bureau(bureau: Bureau):
  #return bureau
  print(type(bureau))
  print(dict(bureau))

  bureau_data = await buro()

  bureau_data=ast.literal_eval(bureau_data)

  bureau_data = dict(bureau_data)

  bureau = dict(bureau)

  print(bureau)
  if bureau_data["check"] == "true":
    data = {
      "check": bureau_data["check"],
      "client_data": str(bureau),
      "bureau_data": str(bureau)
      
    }
  else:
    data = {
      "check": bureau_data["check"],
      "client_data": str(bureau),
      "bureau_data": str(bureau_data["data"])
    }

  await save(data)

  return serializeDict(data)

async def save(bureau):
  print(type(bureau))
  print (bureau)
  await conn.local.check.insert_one(bureau)

#pasar

URL = "http://mock-app:3001/contact"


async def buro():

  client = AsyncClient()

  response = await client.get(URL)
  
  print(response.text)
  return response.text


#context
#Use find() to query for a set of documents. 
#find() does no I/O and does not require an await expression. 
#It merely creates an AsyncIOMotorCursor instance. 
#The query is actually executed on the server when you call to_list() 
#or execute an async for loop.