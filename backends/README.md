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

## Test

```bash
python -m unittest discover tests
```

Watch tests:
```bash
ptw
```

## Deploy

Install production dependencies:

```bash
python -m pip install -r requirements.production.txt
```

```bash
gunicorn
```