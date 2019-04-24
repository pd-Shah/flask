from microblog.models.post import Post
from microblog import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, )
    email = db.Column(db.String(80), unique=True, )
    password_hash = db.Column(db.String(120))
    posts = db.relationship("Post", backref="author", lazy="dynamic")

    def __repr__(self, ):
        return "<User {}>".format(self.username)
