# Flask modules
from flask_login import UserMixin

# Other modules
from datetime import datetime

# Local Modules
from mysales.extensions import db
from mysales.utils.models import generate_uuid


class User(db.Model, UserMixin):
    id = db.Column(
        db.String,
        primary_key=True,
        default=generate_uuid,
        unique=True,
        nullable=False,
    )
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"<User {self.name}>"
