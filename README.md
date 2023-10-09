# flask-api

## Set Environment

```bash
cp .env.example .env
```

## Run DB

```bash
docker compose up -d
```

## Install

```bash
pip3 install -r requirements.txt
```

## Create virtual Environment

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

## How to migrate

```bash
flask db init
```

```bash
flask db migrate
```

```bash
flask db upgrade
```

## Run

```bash
flask --debug run
```
