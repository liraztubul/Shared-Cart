# SharedCart

Shared family shopping list. Anyone adds, anyone checks off, and whatever stayed
unchecked comes back as a report at the end of the trip.

Installable on iPhone and Android as a PWA — no app store.

## Run

```
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env

python -c "from app.db import Base, engine; import app.models; Base.metadata.create_all(engine)"
uvicorn app.main:app --reload
```

- App: http://127.0.0.1:8000
- API docs: http://127.0.0.1:8000/docs

## Install on a phone

Both need the app served over HTTPS, so this works once it is deployed.

- **iPhone** — open the URL in **Safari** (not Chrome) → Share → Add to Home Screen
- **Android** — open in Chrome → menu → Install app / Add to Home screen

## Layout

```
app/
  config.py    settings, DATABASE_URL from env
  db.py        engine, session factory, Base
  deps.py      current_user — the single swap point for auth
  models.py    tables
  main.py      FastAPI app
static/        the PWA: one page, vanilla JS
docs/DESIGN.md decisions and why
```

## Stack

FastAPI · SQLAlchemy 2.0 · SQLite locally, Postgres in production · vanilla JS PWA
