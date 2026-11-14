"""
Four tables. Every one carries household_id.

households   id, name, join_code (unique, index)
users        id, household_id (FK, index), name
items        id, household_id (FK, index), name, quantity, note, status,
             added_by_id, added_at, checked_by_id, checked_at
purchases    id, household_id (FK, index), name, purchased_at

status is one of: needed | bought | unavailable

Three calls to make:
  1. status as a SQLAlchemy Enum, or String(20) validated in code?
     SQLite does not enforce Enum; Postgres does.
  2. Always give String an explicit length. Postgres rejects String without one.
  3. Which index does GET /items need? It runs every 3 seconds and always
     filters on a single household_id.
"""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base

class Household(Base):
    __tablename__ = "households"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    join_code: Mapped[str] = mapped_column(String(20), unique=True, index=True)


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    household_id: Mapped[int] = mapped_column(ForeignKey("households.id"), index=True)
    name: Mapped[str] = mapped_column(String(100))


