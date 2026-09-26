// שלב 1 — השלד. את ממלאת.
//
// 1. loadItems()        GET /items  ומצייר את הרשימה
// 2. setInterval        כל 3 שניות. אל תצייר מחדש אם כלום לא השתנה
// 3. addItem(name)      POST /items
// 4. toggle(id, status) PATCH /items/{id}
// 5. endTrip()          POST /trips/end  ומציג את דוח החסרים
//
// שתי נקודות שקובעות אם זה מרגיש מהיר:
//   - עדכון אופטימי: צובעים את ה-✓ מיד, ומחזירים אחורה אם הבקשה נכשלה
//   - כל בקשה נושאת את הכותרת X-User-Id מ-localStorage

const API = "";

async function api(path, options = {}) {
  const res = await fetch(API + path, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      "X-User-Id": localStorage.getItem("userId") || "",
      ...(options.headers || {}),
    },
  });
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
  return res.status === 204 ? null : res.json();
}

// TODO
