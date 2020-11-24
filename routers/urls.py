from fastapi import APIRouter, HTTPException, Form, Body
from bson import json_util, ObjectId
from pydantic import BaseModel

import pymongo
import json


router = APIRouter()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = myclient["myDatabase"]
url_db = my_db["urlSortenerDB"]

class New_URL(BaseModel):
    url: str


@router.get("/url/")
async def get_urls():
    url_list = list(url_db.find())

    return json.loads(json_util.dumps(url_list))

@router.get("/url/{url_id}")
async def get_url(url_id: str):
    if not(ObjectId.is_valid(url_id)):
        raise HTTPException(status_code=300, detail="url code not valid")
    
    url = url_db.find_one({"_id": ObjectId(url_id)})
    
    if url == None:
        raise HTTPException(status_code=404, detail="url not found")

    return url["origin"]

@router.post("/url/")
async def post_url(new_url: New_URL):
    url = url_db.find_one({"origin": new_url.url})

    if url == None:
        url = url_db.insert_one({"origin": new_url.url})

    return str(url.get("_id"))

@router.put("/url/{url_id}")
async def put_url():
    raise HTTPException(status_code=403, detail="You cant update the id")
