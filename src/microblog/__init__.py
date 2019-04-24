import os

from flask import (
    Flask,
    render_template,)
from microblog.blueprints.auth import login
from microblog.config import Config
from microblog.database import db
from microblog.database import migrate
from microblog.models.post import Post
from microblog.models.user import User


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config.from_pyfile("config.py", silent=False)
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    app.register_blueprint(login.bp, )

    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except Exception as e:
        print(e)

    @app.route("/")
    def index():
        user = {"username": "pd"}
        posts = [
                    {
                        "author": {"username": "John", },
                        "body": "nice day in Iran!"
                        },
                    {
                        "author": {"username": "pd"},
                        "body": "WTF!",
                        },
                ]
        data = {"user": user, "title": "HeLL0", "posts": posts, }
        return render_template("index.html", data=data, )
    return app
