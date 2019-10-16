from main import db
from datetime import date
from main.models.OwnerModel import Owner

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

        # __valid_days is for temporary processing only - not saved to database
        self.__valid_days = 0

    def __repr__(self):
        return (
            f"This instance of Content:\n"
            f"content_name = {self.content_name}\n"
            f"content_type = {self.content_type}\n"
            f"updated_at = {self.updated_at}\n"
            f"valid_months = {self.valid_months}\n"
            f"owner_id = {self.owner_id}"
        )

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

    def get_updated_date(self):
        """returns the updated_at date in a readable format"""
        return self.updated_at.strftime("%b %d, %Y")

    def __calc_days_left(self, months):
        """calculates and sets number of days before content expires"""

        # days passed = today - when content was last updated
        days_passed = (date.today() - self.updated_at).days
        # valid days = total valid days - days passed since last update
        days_left = round(months * 365 / 12) - days_passed
        # __valid_days is set to 0 if negative
        self.__valid_days = days_left if days_left >= 0 else 0

    def get_valid_days(self):
        """returns number of days before content expires"""
        self.__calc_days_left(self.valid_months)
        return self.__valid_days

    def get_owner(self):
        """Returns the name of the owner associated with the owner_id"""
        return Owner.find_by_id(self.owner_id).owner_name
