import os

from flask import request

from app import init_app
from app.api.models import User
from app.utils.objects import Token

app = init_app()


def get_current_user():
    token = request.cookies.get("token")
    try:
        user = User.query.get(Token.decode(token).get("id"))
    except Exception as e:
        user = None
    return user


@app.context_processor
def context_processor():
    return dict(current_user=get_current_user())


if __name__ == "__main__":
    app.run(host="0.0.0.0")
