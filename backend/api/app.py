from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from core.config import settings

from api import sshconn
from api import nodes

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.include_router(sshconn.router, prefix=settings.API_V1_STR)
app.include_router(nodes.router, prefix=settings.API_V1_STR)

@app.get('/')
def root():
    return {'message': 'Hello Topology Map'}

