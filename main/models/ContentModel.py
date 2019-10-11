from main import db

class Content(db.Model):
    __tablename__ = 'contents'

    # contents columns - each content must have a unique name
    id = db.Column(db.Integer, primary_key=True)
    content_name = db.Column(db.String(30), unique=True, nullable=False)
    content_type = db.Column(db.String(), nullable=False)
    updated_at = db.Column(db.Date, nullable=False)
    valid_months = db.Column(db.Integer, nullable=False, default=1)

    # Roles are related to an owner via the owner email field
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    def __init__(self, content_name, content_type, updated_at, valid_months,
                 owner_id):
        self.content_name = content_name
        self.content_type = content_type
        self.updated_at = updated_at
        self.valid_months = valid_months
        self.owner_id = owner_id

    def __repr__(self):
        return f"Content('{self.content_name}', '{self.content_type}')"

    @classmethod
    def find_by_name(cls, name):
        """Finds the content by its unique name and returns it"""
        return cls.query.filter_by(content_name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        """Finds the content by its unique id and returns it"""
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def get_all_content(cls):
        """Returns all content in the contents table"""
        return cls.query.all()

    def save_content(self):
        """Saves the content object to the contents table"""
        db.session.add(self)
        db.session.commit()

    def delete_content(self):
        """Deletes the content object from the contents table"""
        db.session.delete(self)
        db.session.commit()