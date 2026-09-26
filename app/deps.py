"""
נקודת החלפה אחת לזהות.

בשלב 1 המכשיר שולח את מזהה המשתמש בכותרת X-User-Id.
כשיתווסף אימות אמיתי — רק הפונקציה הזאת מתחלפת, ושום endpoint לא נוגע.

TODO: לממש אחרי ש-models.py קיים.
  1. אם אין כותרת -> 401
  2. לשלוף User לפי המזהה -> אין כזה -> 401
  3. להחזיר את ה-User (ומתוכו household_id לכל שאילתה)
"""

from fastapi import Depends, Header
from sqlalchemy.orm import Session

from app.db import get_db


def current_user(
    x_user_id: str | None = Header(default=None),
    db: Session = Depends(get_db),
):
    raise NotImplementedError
