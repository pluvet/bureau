
import ast
import json
import os
import random
import re
from fastapi import APIRouter
import asyncio
from httpx import AsyncClient
from config.db import conn
from models.bureau import Bureau
from models.check import Check
from schemas.bureau import serializeDict, serializeList


bureau = APIRouter()

@bureau.get('/')
async def find_all():
  #  print(conn.local.user.find())
  #  print(serializeList(conn.local.user.find()))
    return serializeList(conn.local.check.find())

@bureau.post('/')
async def check(bureau: Bureau):

  body = await asyncio.gather(request())


  #bureau_data=ast.literal_eval(body[0])
  bureau_data = dict(body)

  if bureau_data["check"] == True:
    data = {
      "check": bureau_data["check"],
      "client_data": bureau.client_data,
      "bureau_data": bureau_data["data"]
      
    }
  else:
    data = {
      "check": bureau_data["check"],
      "client_data": bureau.client_data,
      "bureau_data": bureau.client_data
      
    }

  asyncio.gather(save(data))

  return data

async def save(check: Check):
  print(type(check))
  conn.local.check.insert_one(check)


URL = "http://0.0.0.0:3000/contact"


async def request():

  list_name = {"Juan", "Jose", "Luis", "peter", "candy", "luisa"}
  list_lastname = {"musk", "gray", "kohr", "barranc", "dory", "aeon"}

  cc = str(random.randint(100000, 999999))
  #name = str(random.choice(list_name))
  #lastname= str(random.choice(list_lastname))
  name = "juan"
  lastname = "lopez"
  data = {
    "id_number": cc,
    "name": name,
    "lastname": lastname
  }

  bureau_data = {}

  bureau_data["check"] = bool(random.randint(0,1))
  bureau_data["data"] = data

  return dict(bureau_data)

    #client = AsyncClient()
    #response = await client.get(URL)
    #return response.text

