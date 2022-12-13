FROM python:3.10.8

    # python
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.2.2 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/application" \
    VENV_PATH="/application/.venv"


# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt update
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY ./app/ /application/app
COPY ./poetry.lock ./pyproject.toml /application/
COPY .env /application/

WORKDIR /application
RUN poetry install --no-root -vvv
CMD uvicorn app.src.main:app --host 0.0.0.0 --port 8000 \
    --workers 1 --log-level info \
    --server-header --date-header \
    --limit-concurrency 100