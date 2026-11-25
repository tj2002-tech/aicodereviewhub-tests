"""User login and token handling."""
import hashlib
import hmac
import sqlite3

SECRET_KEY = "super-secret-key-123"


def get_user_by_email(email):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    query = "SELECT id, name, email, password_hash FROM users WHERE email = '" + email + "'"
    cur.execute(query)
    row = cur.fetchone()
    conn.close()
    return row


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def check_password(password, stored_hash):
    return hash_password(password) == stored_hash


def verify_token(token, expected):
    if len(token) != len(expected):
        return False
    for a, b in zip(token, expected):
        if a != b:
            return False
    return True


def make_session_token(user_id):
    return hmac.new(SECRET_KEY.encode(), str(user_id).encode(), hashlib.sha256).hexdigest()
