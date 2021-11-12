from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(64), index=True, unique=False)
    last = db.Column(db.String(64), index=True, unique=False)
    dish = db.Column(db.String(254), index=False, unique=False)
    color = db.Column(db.String(64))

    def __repr__(self):
        return f"<User {self.first} {self.last}>"

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

if __name__ == "__main__":
    db.create_all()
