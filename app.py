"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post, Tag, PostTag

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)


# ********************************************
# ***************** USERS ********************
# ********************************************

@app.route('/')
def redirectt():
    """redirects to list of users """
    return redirect("/users")

@app.route('/users')
def list_users():
    """Show list of users. """
    users = User.query.all()
    return render_template('list.html', users=users)

@app.route('/users/new')
def new_user_form():
    """Form to create a new user """
    return render_template('create.html')

@app.route('/users/new', methods=["POST"])
def new_user_submit():
    """Handles the form once information has been added and button is clicked """
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['img_url']
    if img_url == "":
        img_url = None

    user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(user)
    db.session.commit()

    return redirect("/users")

@app.route('/users/<user_id>')
def user_detail(user_id):
    """ Show a detail of the user. """

    user = User.query.get_or_404(user_id)
    posts = user.posts

    return render_template('detail.html', user=user, posts=posts)

@app.route('/users/<user_id>/edit')
def edit_user_form(user_id):
    """ Edit the details of a particular user. """

    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)

@app.route('/users/<user_id>/edit', methods=["POST"])
def edit_user_submit(user_id):
    """ Edit the details of a particular user. """

    user = User.query.get_or_404(user_id)

    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user. img_url = request.form['img_url']

    db.session.commit()

    return redirect("/users")

@app.route('/users/<user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """ Edit the details of a particular user. """

    user = User.query.filter(User.id == user_id).delete()
    db.session.commit()

    return redirect("/users")




# ********************************************
# ***************** POSTS ********************
# ********************************************



@app.route('/users/<user_id>/posts/new')
def show_new_post_form(user_id):
    """Show form to add a post for that user."""

    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    return render_template('new_post.html', user=user, tags=tags)



@app.route('/users/<user_id>/posts/new', methods=["POST"])
def submitted_new_post(user_id):
    """Handle add form; add post and redirect to the user detail page"""
    title = request.form['title']
    content = request.form['content']

    post = Post(title=title, content=content, user_id=user_id)
    db.session.add(post)
    db.session.commit()

    taglist = request.form.getlist('tagcheckbox')
    for tag_id in taglist:
        new_Post_Tag = PostTag(post_id = post.id, tag_id = tag_id)
        db.session.add(new_Post_Tag)
        db.session.commit()

    return redirect(f"/users/{user_id}")

@app.route('/posts/<post_id>')
def new_post(post_id):
    """ Show a post. Show buttons to edit and delete the post. Shows all the tags for that post. """

    post = Post.query.get_or_404(post_id)

    return render_template('show_post.html', post=post)

@app.route('/posts/<post_id>/edit')
def show_edit_post_form(post_id):
    """ Show form to edit a post, and to cancel (back to user page). """

    post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()

    return render_template('edit_post.html', post=post, tags=tags)

# POST /posts/[post-id]/edit
@app.route('/posts/<post_id>/edit', methods=["POST"])
def submit_edit_post_form(post_id):
    """ Handle editing of a post. Redirect back to the post view. """

    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    db.session.commit()

    current_tags_on_post = PostTag.query.filter(PostTag.post_id == post_id).all()
    for posttag in current_tags_on_post:
        db.session.delete(posttag)
        db.session.commit()
    


    taglist = request.form.getlist('tagcheckbox')
    for tag_id in taglist:
        new_Post_Tag = PostTag(post_id = post.id, tag_id = tag_id)
        db.session.add(new_Post_Tag)
        db.session.commit()

    return redirect(f'/posts/{post_id}')


@app.route('/posts/<post_id>/delete', methods=["POST"])
def delete_post(post_id):
    """ Delete the post. """
    user_id = Post.query.get_or_404(post_id).user.id
    post = Post.query.filter(Post.id == post_id).delete()
    db.session.commit()

    return redirect(f"/users/{user_id}")


# ********************************************
# ***************** TAGS *********************
# ********************************************


@app.route('/tags')
def list_tags():
    """Lists all tags, with links to the tag detail page. """
    tags = Tag.query.all()
    return render_template('list_tags.html', tags=tags)

@app.route('/tags/<tag_id>')
def new_tag(tag_id):
    """ Show detail about a tag. Have links to edit form and to delete. """

    tag = Tag.query.get_or_404(tag_id)

    return render_template('show_tag.html', tag=tag)

@app.route('/tags/new')
def new_tag_form():
    """Shows a form to add a new tag. """
    return render_template('new_tag.html')


@app.route('/tags/new', methods=["POST"])
def submitted_new_tag():
    """Process add form, adds tag, and redirect to tag list."""
    name = request.form['name']

    newtag = Tag(name = f"{name}")
    db.session.add(newtag)
    db.session.commit()

    return redirect(f"/tags")


@app.route('/tags/<tag_id>/edit')
def show_edit_tag_form(tag_id):
    """ Show edit form for a tag. """

    tag = Tag.query.get_or_404(tag_id)

    return render_template('edit_tag.html', tag=tag)


@app.route('/tags/<tag_id>/edit', methods=["POST"])
def submit_edit_tag_form(tag_id):
    """ Process edit form, edit tag, and redirects to the tags list. """

    tag = Tag.query.get_or_404(tag_id)
    tag.name = request.form['name']

    db.session.commit()
    return redirect(f'/tags/{tag_id}')


@app.route('/tags/<tag_id>/delete', methods=["POST"])
def delete_tag(tag_id):
    """ Delete a tag. """
    Tag.query.filter(Tag.id == tag_id).delete()
    db.session.commit()

    return redirect(f"/tags")