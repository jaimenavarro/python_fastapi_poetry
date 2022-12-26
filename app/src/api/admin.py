import asyncio
import logging

import httpx
from fastapi import APIRouter
from time import sleep

# get root logger
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project.

router = APIRouter()


@router.get("/async")
async def root():
    logger.warning("TESTING async")
    headers = {'User-Agent': 'curl/7.79.1'}
    await asyncio.sleep(10)
    client = httpx.AsyncClient()
    r = await client.get('http://ifconfig.me', headers=headers)
    return r.text


@router.get("/sync")
def root():
    logger.warning("TESTING sync")
    headers = {'User-Agent': 'curl/7.79.1'}
    sleep(10)
    r = httpx.get('http://ifconfig.me', headers=headers)
    return r.text
