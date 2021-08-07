from unittest import TestCase

from app import app
from models import db, User

# access a testdatabase, rather than your actual database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

# now flask errors will be real errors, rather than HTML pages
app.config['TESTING'] = True

# don't use flask debug toolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserTestCase(TestCase):
    """Tests for """

    def setUp(self):
        """Add sample user."""

        User.query.delete()

        user = User(first_name="TEST_FIRST_NAME", last_name="TEST_LAST_NAME", img_url="https://spng.pngfind.com/pngs/s/123-1234419_free-png-download-cute-cat-png-images-background.png")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        """Clean up all transactions."""

        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 302)

    def test_list_users_redirect(self):
        with app.test_client() as client:
            resp = client.get("/", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>USERS</h1>", html)

    def test_new_user_submit(self):
        with app.test_client() as client:
            d = {"first_name": "TestUser2-first-name", "last_name": "TestUser2-last-name", "img_url": "TestUser2-img-url"}
            resp = client.post("/users/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("TestUser2-first-name", html)
            self.assertIn("TestUser2-last-name", html)

    