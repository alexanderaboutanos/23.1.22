from models import User, Post, db
from app import app

# create all tables
db.drop_all()
db.create_all()

# Make a bunch of posts
post1 = Post(title="Post1", content="Well, this is just me, sayig hello", user_id="1")
post2 = Post(title="Post2", content="I love you", user_id="2")
post3 = Post(title="Post3", content="Guess what? Jesus is King!", user_id="3")
post4 = Post(title="Post4", content="Is it dinner time already?", user_id="3")
post5 = Post(title="Post5", content="Syriac is a superior language... we all know it.", user_id="4")
post6 = Post(title="Post6", content="Greek isn't the best language... we all know it.", user_id="3")

db.session.add_all([post1, post2, post3, post4, post5, post6])

# db.session.commit()

# Make a bunch of users
user1 = User(first_name = "John", last_name = "Doe")
user2 = User(first_name = "Jimminy", last_name = "Cricket")
user3 = User(first_name = "Paul", last_name = "Mall")
user4 = User(first_name = "Jack", last_name = "Rabbit")
user5 = User(first_name = "Bees", last_name = "Knees")

db.session.add_all([user1, user2, user3, user4, user5])

db.session.commit()