from flask import session, redirect, url_for, request
from functools import wraps


def login_required(f):
    @wraps(f)
    def check(*args, **kwargs):
        if not session.get("cus"):
            return redirect(url_for("login", next=request.url))

        return f(*args, **kwargs)

    return check
