from flask import (
        Blueprint,
        render_template,
        redirect,
        url_for,
        flash,
        )
from microblog.forms.auth.login import LoginForm

bp = Blueprint("login", __name__, url_prefix="/login")


@bp.route("/", methods=["POST", "GET", ])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(form.username.data, form.remember_me.data)
        return redirect(url_for("index"))
    return render_template("auth/login.html", form=form)
