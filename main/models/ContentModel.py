from datetime import date

from main import db


class Content(db.Model):
    __tablename__ = 'contents'

    # contents columns
    id = db.Column(db.Integer, primary_key=True)
    content_name = db.Column(db.String(30), unique=True, nullable=False)
    content_type = db.Column(db.String(), nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False, default=date.today)
    valid_months = db.Column(db.Integer, nullable=False, default=1)

    # One role relates to one user
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'), nullable=False)

    def __repr__(self):
        return f"Content('{self.content_name}', '{self.content_type}')"
