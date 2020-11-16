from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello Web Development Team"}

@app.get("/short/{url}")
async def root(url: str):
    web_url = "http://tinyurl.com/api-create.php?url=" + url
    r = requests.get(web_url)
    return r.text