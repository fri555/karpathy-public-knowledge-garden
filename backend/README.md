# Backend

FastAPI backend for the public knowledge garden review-card app.

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Test

```bash
PYTHONPATH=. pytest
```

## Export Static Data

```bash
PYTHONPATH=. python -m app.export_cards
```
