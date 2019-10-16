import unittest
from datetime import date

from main.models.ContentModel import Content

class ContentModelTests(unittest.TestCase):
    """test_content is used as the test object for methods in Content"""
    test_content = Content(
        content_name="Test Content",
        content_type="Video",
        updated_at=date(2019, 10, 15),
        valid_months=2,
        owner_id=0
    )

    def test_get_updated_date(self):
        """
        get_updated_date() should return a date in the string format of:
        3-letter month followed by DD, YYYY
        """
        self.assertEqual(
            self.test_content.get_updated_date(),
            "Oct 15, 2019"
        )

    def test_Content_repr(self):
        """
        printing a Content object should return the content's instance fields:
        """
        self.assertEqual(
            self.test_content.__repr__(),
            "This instance of Content:\n"
            "content_name = Test Content\n"
            "content_type = Video\n"
            "updated_at = 2019-10-15\n"
            "valid_months = 2\n"
            "owner_id = 0"
        )

if __name__ == "__main__":
    unittest.main()
