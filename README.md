# mini-rag-app

A domain-specific **Retrieval-Augmented Generation (RAG)** system for the **gym & health** domain — built on top of a FastAPI backend with a full production-style pipeline (vector search, LLM augmentation, background processing, and monitoring).

## Overview

`mini-rag-app` lets users upload domain documents (gym/health related content), processes and indexes them into a vector store, and answers questions using semantic search + LLM-generated, context-augmented responses.

## Requirements

- Python 3.10

#### Install Dependencies

```bash
sudo apt update
sudo apt install libpq-dev gcc python3-dev
```

#### Install Python using MiniConda

1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2) Create a new environment:
```bash
$ conda create -n mini-rag-app python=3.10
```
3) Activate the environment:
```bash
$ conda activate mini-rag-app
```

### (Optional) Improve your shell prompt readability

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file (e.g. `OPENAI_API_KEY`).

### Run Alembic Migration

```bash
$ alembic upgrade head
```

## Run Docker Compose Services

```bash
$ cd docker
$ cp .env.example .env
```

- update `.env` with your credentials

```bash
$ cd docker
$ sudo docker compose up -d
```

## Access Services

- **FastAPI**: http://localhost:8000
- **Flower Dashboard**: http://localhost:5555 (admin/password from env)
- **Grafana**: http://localhost:3000
- **Prometheus**: http://localhost:9090

## Run the FastAPI server (Development Mode)

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## Celery (Development Mode)

For development, you can run Celery services manually instead of using Docker.

Run the **Celery worker** (in a separate terminal):

```bash
$ python -m celery -A celery_app worker --queues=default,file_processing,data_indexing --loglevel=info
```

Run the **Beat scheduler** (in a separate terminal):

```bash
$ python -m celery -A celery_app beat --loglevel=info
```

Run the **Flower Dashboard** (in a separate terminal):

```bash
$ python -m celery -A celery_app flower --conf=flowerconfig.py
```

Open your browser at `http://localhost:5555` to view the dashboard.

## Tech Stack

- **API**: FastAPI
- **Database**: PostgreSQL + pgvector (via SQLAlchemy & Alembic)
- **Background Processing**: Celery (workers + beat scheduler)
- **Monitoring**: Flower, Grafana, Prometheus
- **Containerization**: Docker & Docker Compose
- **LLM / Embeddings**: pluggable LLM factory (OpenAI / Ollama-compatible)

## POSTMAN Collection

Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)