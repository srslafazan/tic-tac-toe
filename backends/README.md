# Tic Tac Toe - Backends

## Prerequisites

- Set up your `.venv`
- Install the library


## Setup (development)

Activate your `.venv` if you haven't already:

```bash
source ../.venv/bin/activate
```

Install dependencies:

```bash
python -m pip install pyproject.toml
python -m pip install -r requirements.txt
python -m pip install -r requirements.development.txt
```


## Start

```bash
python -m api.app
```

The API development server runs on http://127.0.0.1:5000/ by default.

> View the production docs at https://tic-tac-toe-backends.fly.dev/docs
> View the local docs at http://127.0.0.1:5000/docs

## Test

```bash
python -m coverage run -m unittest discover tests
```

Watch tests:
```bash
ptw
```

Report coverage:
```bash
python -m coverage report
```

## Deploy

Install production dependencies:

```bash
python -m pip install -r requirements.production.txt
```

Run:

```bash
gunicorn wsgi:app
```