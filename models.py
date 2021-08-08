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

    img_url = db.Column(db.String(5000),
                    nullable = False,
                    default = 'https://www.cpd-umanitoba.com/wp-content/uploads/2016/08/profile-missing.png')

    def __repr__(self):
        """Show info about the user. """

        u = self
        return f"<User #{u.id}, {u.first_name} {u.last_name}>"

class Post(db.Model):
    """Post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)
    
    title = db.Column(db.String(50),
                    nullable = False)

    content = db.Column(db.Text,
                    nullable = False)

    created_at = db.Column(db.DateTime(timezone=True),
                    server_default=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref='posts')

    def __repr__(self):
        """Show info about the user. """

        p = self
        return f"<Post #{p.id}, {p.title}, {p.created_at}>"