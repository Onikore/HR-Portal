import uvicorn
from fastapi import FastAPI

from app.api.api_v1.api import api_router
from app.db.session import db

app = FastAPI(title='HR Cab', openapi_url='/api/v1/openapi.json', version='0.0.1')
app.include_router(api_router)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=5000, reload=True)
