from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    food = db.Column(db.String(254), index=False, unique=False)
    penguin = db.Column(db.String(64))

    def __repr__(self):
        return f"<User {self.username}, food={self.food}, penguin={self.penguin}>"


if __name__ == "__main__":
    db.create_all()
