from main import db

class Owner(db.Model):
    __tablename__ = 'owners'

    # owners columns - each owner must have an unique email
    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String(20), nullable=False)
    owner_email = db.Column(db.String(50), unique=True, nullable=False)
    joined_at = db.Column(db.Date, nullable=False)

    # each owner can relate to many contents
    # relationship(ChildClass, reference_variable, lazy_loading)
    contents = db.relationship('Content', backref='owner', lazy=True)

    def __init__(self, owner_name, owner_email, joined_at):
        self.owner_name = owner_name
        self.owner_email = owner_email
        self.joined_at = joined_at

    def __repr__(self):
        return ("This instance of Owner:\n"
                f"owner_name = {self.owner_name}\n"
                f"owner_email = {self.owner_email}\n"
                f"joined_at = {self.joined_at}")

    @classmethod
    def find_by_email(cls, email):
        """Returns the first owner record matching the correct email"""
        return cls.query.filter_by(owner_email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        """Returns the first owner record matching the correct id"""
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def get_all_owners(cls):
        """Returns all the owners in the owners table"""
        return cls.query.all()

    def get_joined_date(self):
        """returns the joined_at date in a readable format"""
        return self.joined_at.strftime("%b %d, %Y")

    def save_owner(self):
        """Saves an owner to the owners table"""
        db.session.add(self)
        db.session.commit()

    def delete_owner(self):
        """Deletes an owner from the owners table"""
        db.session.delete(self)
        db.session.commit()
