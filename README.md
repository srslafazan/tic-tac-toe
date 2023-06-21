# Tic Tac Toe

A stateless tic-tac-toe implementation in Python that supports human and/or computer players.

[![Tests](https://github.com/srslafazan/tic-tac-toe/actions/workflows/test.yml/badge.svg)](https://github.com/srslafazan/tic-tac-toe/actions/workflows/tests.yml)

## TL;DR

```bash
python -m frontends.console -X human -O minimax
```


## Usage

### Requirements

- python 3.11.4
- pip 23.1.2
- virtualenv 20.21.0

### Setup

> Note: use Python 3

Set up a virtualenv:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the library:

```bash
python -m pip install --editable library/
```

### Further Documentation

The backend may be run as standalone API services.

> See the [Backends README](backends/README.md)

The game may be played via console.

> See the [Frontends README](frontends/README.md)


## License

MIT

See [LICENSE](LICENSE)

