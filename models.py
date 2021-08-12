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

    tags = db.relationship('Tag', secondary='post_tags', backref='posts')

    def __repr__(self):
        """Show info about the user. """

        p = self
        return f"<Post #{p.id}, {p.title}, {p.created_at}>"

class Tag(db.Model):
    """Tag."""

    __tablename__ = "tags"

    id = db.Column(db.Integer,
                    autoincrement = True,
                    primary_key = True)

    name = db.Column(db.String(50),
                    unique = True)

    def __repr__(self):
        """Show info about the tag. """

        t = self
        return f"<Tag #{t.id}, {t.name}>"


class PostTag(db.Model):
    """PostTag."""

    __tablename__ = "post_tags"

    post_id = db.Column(db.Integer,
                    db.ForeignKey("posts.id"),
                    primary_key = True)

    tag_id = db.Column(db.Integer,
                    db.ForeignKey("tags.id"),
                    primary_key = True)

    def __repr__(self):
        """Show info about the post tag. """

        pt = self
        return f"<PostTag #{pt.post_id}, {pt.tag_id} >"