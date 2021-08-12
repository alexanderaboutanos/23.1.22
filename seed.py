from models import User, Post, db, Tag, PostTag
from app import app

# create all tables
db.drop_all()
db.create_all()

# Make a bunch of posts
post1 = Post(title="Post1", content="Well, this is just me, saying hello", user_id="1")
post2 = Post(title="Post2", content="I love you", user_id="2")
post3 = Post(title="Post3", content="Guess what? Jesus is King!", user_id="3")
post4 = Post(title="Post4", content="Is it dinner time already?", user_id="3")
post5 = Post(title="Post5", content="Syriac is a superior language... we all know it.", user_id="4")
post6 = Post(title="Post6", content="Greek isn't the best language... we all know it.", user_id="3")

db.session.add_all([post1, post2, post3, post4, post5, post6])

# Make a bunch of users
user1 = User(first_name = "John", last_name = "Doe")
user2 = User(first_name = "Jimminy", last_name = "Cricket")
user3 = User(first_name = "Paul", last_name = "Mall")
user4 = User(first_name = "Jack", last_name = "Rabbit")
user5 = User(first_name = "Bees", last_name = "Knees")

db.session.add_all([user1, user2, user3, user4, user5])

tag1 = Tag(name = "Fun!")
tag2 = Tag(name = "Loving")
tag3 = Tag(name = "Mean")
tag4 = Tag(name = "Kind")
tag5 = Tag(name = "True")

db.session.add_all([tag1, tag2, tag3, tag4, tag5])

db.session.commit()

post_tag1 = PostTag(post_id = 1, tag_id = 2)
post_tag2 = PostTag(post_id = 3, tag_id = 4)
post_tag3 = PostTag(post_id = 1, tag_id = 4)
post_tag4 = PostTag(post_id = 3, tag_id = 5)
post_tag5 = PostTag(post_id = 2, tag_id = 2)
post_tag6 = PostTag(post_id = 5, tag_id = 3)
post_tag7 = PostTag(post_id = 5, tag_id = 1)
post_tag8 = PostTag(post_id = 2, tag_id = 4)
post_tag9 = PostTag(post_id = 6, tag_id = 3)

db.session.add_all([post_tag1, post_tag2, post_tag3, post_tag4, post_tag5, post_tag6, post_tag7, post_tag8, post_tag9])


db.session.commit()