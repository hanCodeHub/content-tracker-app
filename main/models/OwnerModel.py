from datetime import date

from main import db


class Owner(db.Model):
    __tablename__ = 'owners'

    # owners columns
    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String(20), nullable=False)
    owner_email = db.Column(db.String(50), unique=True, nullable=False)
    joined_at = db.Column(db.DateTime, nullable=False, default=date.today)

    # each owner can relate to many contents
    contents = db.relationship('Content', backref='owners', lazy=True)

    def __repr__(self):
        return f"Owner('{self.owner_name}','{self.owner_email}')"