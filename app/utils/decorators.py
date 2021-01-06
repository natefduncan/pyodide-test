from functools import wraps

from flask import redirect, request, url_for

from app.api.models import User
from app.utils.objects import Token


def login_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.cookies.get("token")
            try:
                user_data = Token.decode(token)
                return f(*args, **kwargs)
            except:
                return redirect(url_for("auth.login"))

        return decorated_function

    return decorator


def permissions(tags):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.cookies.get("token")
            try:
                user_data = Token.decode(token)
            except:
                return redirect(url_for("auth.login"))

            if user_data:
                user = User.query.get(user_data.get("id"))
                if user.get("permissions"):
                    if user.get("permissions") in set(tags):
                        return f(*args, **kwargs)
                    else:
                        return redirect(url_for("auth.no_auth"))
                else:
                    return redirect(url_for("auth.no_auth"))
            else:
                return redirect(url_for("auth.login", next=request.url))

        return decorated_function

    return decorator
