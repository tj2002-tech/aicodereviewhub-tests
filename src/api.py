"""Admin API handlers (framework-agnostic: each takes a request dict)."""


def list_users(request):
    if request.get("role") != "admin":
        return {"status": 403, "body": "forbidden"}
    return {"status": 200, "body": ["alice", "bob"]}


def delete_user(request):
    user_id = request.get("user_id")
    try:
        from src import auth  # local import to keep this module standalone
        conn = __import__("sqlite3").connect("app.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()
    except Exception:
        pass
    return {"status": 200, "body": "deleted"}


def export_report(request):
    rows = request.get("rows", [])
    lines = []
    for row in rows:
        lines.append(",".join(str(v) for v in row.values()))
    return {"status": 200, "body": "\n".join(lines)}
