# Example Python with FastAPI, MySQL, Redis
Follow links shows information about the requirements used for this microservice:
* [Poetry](https://python-poetry.org/docs/#installation)
* [WSGI uvicorn](https://www.uvicorn.org/settings/)
* [FastAPI](https://fastapi.tiangolo.com/tutorial/)
    *   [FastAPI concurrency and async / await operations](https://fastapi.tiangolo.com/async/)
* [SQL Database](https://fastapi.tiangolo.com/tutorial/sql-databases)
* [Redis Database](https://pypi.org/project/redis/)
* [python-decouple - config options](https://pypi.org/project/python-decouple/)

## Folders
```shell
└─╾ tree -L 2 .
.
├── README.md
├── __pycache__
├── app
│   ├── __pycache__
│   ├── src
│   └── tests
├── docker
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs
│   └── img.png
├── helm
│   └── py_fastapi_poetry
├── poetry.lock
├── pyproject.toml
└── python_fastapi_poetry.iml
```

## Python Build and Run
We use [Poetry](https://python-poetry.org/docs/#installation) for the following actions.

* Create virtualenv configuration and install current dependencies
```shell
poetry install
```

* Install new dependencies
```shell
poetry add [dependencies]
```

* Run app
```shell
python -m uvicorn app.src.main:app --reload 
```

## Docker Details
### Build Docker Image
```shell
docker build . -f docker/Dockerfile
```

### Run Docker Compose with MySQL and Redis 
```shell
docker-compose -f docker/docker-compose.yml up
```

## Helm
* Download dependencies (MySQL and Redis)
```shell
helm dep up helm/py_fastapi_poetry
```

* Deploy chart and dependencies
```shell
helm upgrade py helm/py_fastapi_poetry/ -i --debug
```

* Uninstall charts
```shell
helm uninstall py
kubectl delete pvc -l app.kubernetes.io/instance=py
```

## API Documents
* http://0.0.0.0:8000/docs

![img.png](docs/img.png)