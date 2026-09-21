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

Format the source code:

```bash
uv run ruff format src
```

Run formatting checks:

```bash
uv run ruff format --check src
```

Run linting:

```bash
uv run ruff check src
```

Run static type checking:

```bash
uv run mypy src
```
