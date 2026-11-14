// Stage 1 skeleton. Fill these in.
//
// 1. loadItems()        GET /items, render the list
// 2. setInterval        every 3s; skip the re-render when nothing changed
// 3. addItem(name)      POST /items
// 4. toggle(id, status) PATCH /items/{id}
// 5. endTrip()          POST /trips/end, show the missing-items report
//
// Two things decide whether this feels fast:
//   - optimistic update: paint the check immediately, roll back if the request fails
//   - every request carries the X-User-Id header from localStorage

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
