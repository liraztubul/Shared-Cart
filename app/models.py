"""
ארבע טבלאות. כולן נושאות household_id.

households
    id, name, join_code (unique, index)

users
    id, household_id (FK, index), name

items                                     הרשימה הפעילה
    id, household_id (FK, index), name, quantity, note,
    status            needed | bought | unavailable
    added_by_id       FK -> users.id
    added_at
    checked_by_id     FK -> users.id, nullable
    checked_at        nullable

purchases                                 היסטוריה, מקור הדאטה לדירוג בשלב 2
    id, household_id (FK, index), name, purchased_at


שלוש הכרעות שלך:

  1. status — Enum של SQLAlchemy או String(20) עם בדיקה בקוד?
     (רמז: SQLite לא אוכף Enum, Postgres כן. מה זה אומר על בדיקות מקומיות?)

  2. String(n) תמיד עם אורך מפורש. Postgres ידחה String בלי אורך,
     וזה יתגלה רק ביום הפריסה.

  3. איזה index דרוש כדי ש-GET /items יהיה מהיר?
     הוא רץ כל 3 שניות, והשאילתה היא תמיד
     "כל ה-items של household_id אחד".
"""

from app.db import Base  # noqa: F401

# TODO
