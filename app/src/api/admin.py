import asyncio
import logging

import httpx
from fastapi import APIRouter
from time import sleep

# get logger
logger = logging.getLogger(__name__)  # the __name__ resolve to this package

router = APIRouter()


@router.get("/async")
async def root():
    logger.debug("TESTING async")
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
