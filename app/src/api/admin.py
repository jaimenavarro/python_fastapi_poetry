from fastapi import APIRouter
import requests

router = APIRouter()


@router.get("/")
def root():
    headers = {'User-Agent': 'curl/7.79.1'}
    r = requests.get('http://ifconfig.me', headers=headers)
    return r.text
