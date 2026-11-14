"""
Single swap point for identity.

Stage 1: the device sends its user id in the X-User-Id header.
When real auth arrives, only this function changes — no endpoint is touched.

TODO: implement once models.py exists.
  1. no header            -> 401
  2. no User with that id -> 401
  3. return the User (its household_id scopes every query)
"""

from fastapi import Depends, Header
from sqlalchemy.orm import Session

from app.db import get_db


def current_user(
    x_user_id: str | None = Header(default=None),
    db: Session = Depends(get_db),
):
    raise NotImplementedError
