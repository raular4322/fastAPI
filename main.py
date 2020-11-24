from fastapi import Depends, FastAPI, Header, HTTPException

from routers import urls, home


app = FastAPI()

app.include_router(urls.router)
app.include_router(home.router)
