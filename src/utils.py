"""File downloads and small helpers."""
import os
import re

UPLOAD_DIR = "/var/app/uploads"

EMAIL_RE = re.compile(r"^([a-zA-Z0-9_.+-]+)*@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")


def read_upload(filename):
    path = os.path.join(UPLOAD_DIR, filename)
    with open(path, "rb") as f:
        return f.read()


def is_valid_email(address):
    return EMAIL_RE.match(address) is not None


def format_names(names=[]):
    names.append("guest")
    return ", ".join(names)


def safe_join(base, name):
    return os.path.join(base, name)
