# Example Python with FastAPI, MySQL, Redis
* [FastAPI](https://fastapi.tiangolo.com/tutorial/)
* [SQL Database](https://fastapi.tiangolo.com/tutorial/sql-databases)
* [Redis Database](https://pypi.org/project/redis/)

## Folders
```shell
└─╾ tree -L 2 .
.
├── README.md
├── __pycache__
├── doc
├── docker
│   ├── Dockerfile
│   └── docker-compose.yml
├── poetry.lock
├── pyproject.toml
├── python_fastapi_poetry.iml
├── src
│   ├── __init__.py
│   ├── __pycache__
│   ├── main.py
│   ├── redis_db
│   └── sql_db
└── test_main.http
```

## Docker Details
### Build Docker Image
```shell
┌─[jaime@jaime-mac-pro]─[~/Documents/Local/python_fastapi_poetry]─[]
└─╾ docker build . -f docker/Dockerfile
```

### Docker Compose with all dependencies 
```shell
┌─[jaime@jaime-mac-pro]─[~/Documents/Local/python_fastapi_poetry]─[]
└─╾ docker-compose -f docker/docker-compose.yml up
```

## API Documents
* http://0.0.0.0:8000/docs

![img.png](docs/img.png)

