import asyncio
import logging

import httpx
from fastapi import APIRouter
from starlette.requests import Request
from time import sleep

# get logger
logger = logging.getLogger(__name__)  # the __name__ resolve to this package

router = APIRouter()


@router.get("/async")
async def root(request: Request):
    logger.debug("TESTING async")
    iterator = ((i, request.headers.get(i)) for i in request.headers.keys())
    logger.debug("Client Host: " + request.client.host + " Headers: " + list(iterator).__str__())
    headers = {'User-Agent': 'curl/7.79.1'}
    await asyncio.sleep(10)
    client = httpx.AsyncClient()
    r = await client.get('http://ifconfig.me', headers=headers)
    return r.text


@router.get("/sync")
def root():
    logger.debug("TESTING sync")
    headers = {'User-Agent': 'curl/7.79.1'}
    sleep(10)
    r = httpx.get('http://ifconfig.me', headers=headers)
    return r.text
