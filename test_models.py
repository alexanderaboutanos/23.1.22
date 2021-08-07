from unittest import TestCase

from app import app
from models import db, User

# access a testdatabase, rather than your actual database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    """ Tests for model for Users."""

    def setUp(self):
        User.query.delete()
    
    def tearDown(self):
        db.session.rollback()
    
    def test_user(self):
        first_user = User(first_name="A_FIRST_NAME", last_name="A_LAST_NAME", img_url="https://spng.pngfind.com/pngs/s/123-1234419_free-png-download-cute-cat-png-images-background.png")
        second_user = User(first_name="ANOTHER_FIRST_NAME", last_name="ANOTHER_LAST_NAME", img_url="https://www.vhv.rs/dpng/d/457-4575780_cat-isolated-cut-out-kitten-white-pet-animal.png")

        db.session.add(first_user)
        db.session.add(second_user)
        db.session.commit()

        user_1 = User.query.get(1)
        user_2 = User.query.get(2)

        self.assertEquals(user_1, first_user)
        self.assertEquals(user_2, second_user)








