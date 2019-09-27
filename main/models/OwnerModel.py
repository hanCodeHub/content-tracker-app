from main import db


class Owner(db.Model):
    __tablename__ = 'owners'

    # owners columns
    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String(20), nullable=False)
    owner_email = db.Column(db.String(50), unique=True, nullable=False)
    joined_at = db.Column(db.DateTime, nullable=False)

    # each owner can relate to many contents
    contents = db.relationship('Content', backref='owners', lazy=True)

    def __init__(self, owner_name, owner_email, joined_at):
        self.owner_name = owner_name
        self.owner_email = owner_email
        self.joined_at = joined_at

    def __repr__(self):
        return f"Owner('{self.owner_name}','{self.owner_email}')"

    @classmethod
    def find_by_email(cls, email):
        # query rows with the correct email, and fetch the first record
        return cls.query.filter_by(owner_email=email).first()

    @classmethod
    def find_by_name(cls, name):
        # query rows with the correct owner name, and fetch all records
        return cls.query.filter_by(owner_name=name).all()

    @classmethod
    def get_all_owners(cls):
        return cls.query.all()

    def save_owner(self):
        # add() creates a new record if not exist, otherwise updates existing
        db.session.add(self)
        db.session.commit()

    def delete_owner(self):
        db.session.delete(self)
        db.session.commit()
