FROM python:3-slim-buster 

WORKDIR /hero-app-v2

COPY requirements.txt /hero-app-v2/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /hero-app-v2/requirements.txt

COPY . /hero-app-v2

# CMD ["sh", "-c", "alembic upgrade head && tail -f /dev/null"]
CMD ["sh", "-c", "alembic upgrade head && python -m app.entrypoints"]

# FROM python:3.10-slim-buster

# ENV PYTHONFAULTHANDLER=1 \
#     PYTHONUNBUFFERED=1 \
#     PYTHONHASHSEED=random \
#     PIP_NO_CACHE_DIR=off \
#     PIP_DISABLE_PIP_VERSION_CHECK=on \
#     PIP_DEFAULT_TIMEOUT=100 \
#     POETRY_VERSION=1.6.1

# # System deps:
# RUN pip install "poetry==$POETRY_VERSION"

# # Copy only requirements to cache them in docker layer
# WORKDIR /backend
# COPY poetry.lock pyproject.toml /backend/


# # Project initialization:
# RUN poetry config virtualenvs.create false \
#     && poetry install --no-interaction --no-ansi

# # Creating folders, and files for a project:
# COPY . /backend/

# CMD ["sh", "-c", "alembic upgrade head && python -m app.entrypoints"]