"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to Database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)
    
    first_name = db.Column(db.String(50),
                    nullable = False)

    last_name = db.Column(db.String(50),
                    nullable = False)

    img_url = db.Column(db.Text,
                    default = 'https://www.cpd-umanitoba.com/wp-content/uploads/2016/08/profile-missing.png')

    def __repr__(self):
        """Show info about the user. """

        u = self
        return f"<User #{u.id}, {u.first_name} {u.last_name}>"