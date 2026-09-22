# Learning Buddy
An application that helps you learn and retain knowledge.

## Requirements

- Python 3.12+
- uv

## Setup

Install the project dependencies:
```bash
uv sync
```

## Running

```bash
uv run learning-buddy
```

## Code quality

The project uses [Ruff](https://docs.astral.sh/ruff/) for formatting and linting and [mypy](https://mypy.readthedocs.io/) for static type checking.

Format the source code:

```bash
uv run ruff format src tests
```

Run formatting checks:

```bash
uv run ruff format --check src tests
```

Run linting:

```bash
uv run ruff check src tests
```

Run static type checking:

```bash
uv run mypy src tests
```

## Testing

This project uses pytest for automated testing. Unit and integration tests are organized separately and can be run independently.

Run the complete test suite:

```bash
uv run pytest
```

Run only unit tests:

```bash
uv run pytest tests/unit
```


Run only integration tests:

```bash
uv run pytest tests/integration
```

Run the complete test suite with coverage:

```bash
uv run pytest --cov=learning_buddy
```
