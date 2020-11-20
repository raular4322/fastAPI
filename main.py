from fastapi import FastAPI, HTTPException
import pymongo

app = FastAPI()
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = myclient["myDatabase"]
url_db = my_db["urlSortenerDB"]

@app.get("/")
async def root():
    return {"message":"Hello Web Development Team"}

@app.get("/short/all")
async def get_url_list():
    for x in url_db.find({}):
        print(x)
    return url_db.find({})

@app.get("/short/{url}")
async def get_url(url: str):
    url_in_db = url_db.find_one({"originURL": url})

    if url_in_db == None:
        raise HTTPException(status_code=404, detail="url not found in DB")

    return url_in_db["originURL"]

@app.post("/short/{url}")
async def post_url(url: str):
    url_in_db = url_db.find_one({"originURL": url})

    if url_in_db != None:
        raise HTTPException(status_code=300, detail="url already in db")

    url_in_db = url_db.insert_one({"originURL": url})
    return url_in_db["_id"]
