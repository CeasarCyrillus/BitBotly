from init_app import *
from flask import render_template, request, redirect, url_for, g, flash
from forms import Signup_form, Login_form, Post_form, Contact_form
from flask_login import login_user, logout_user, current_user, login_required
import datetime
from api_utils import Response
def Base():
    data = {
        "forms":{},
        "errors":{}
        }
    return data

@app.before_request
def before_request():
    g.user = current_user
    if current_user.is_authenticated and current_user.is_authenticated():
        g.logged_in = True
    else:
        g.logged_in = False

@app.errorhandler(404)
def page_not_found(e):
    return render_template('templates/404.html'), 404

@app.route("/", methods=["GET", "POST"])
def home():
    data = Base()
    return render_template("templates/index.html", data=data)

@app.route("/blog")
def blog():
    data = Base()
    posts = Post.query.all()
    data["posts"] = posts
    
    return render_template("templates/blog.html", data=data)

@app.route("/blog/<post_url_title>")
def blogpost(post_url_title):
    data = Base()

    post = Post.query.filter(Post.url_title == post_url_title).first()
    if not post:
        return "sorry", 404
    data["post"] = post
    return render_template("templates/post.html", data=data)

@app.route("/blog/new-post", methods=["GET", "POST"])
@app.route("/blog/new-post/<post_to_edit>", methods=["GET", "POST"])
def new_post(post_to_edit=None):
    data = Base()
    new_post_form = Post_form(prefix="new_post")
    data["forms"]["new_post_form"] = new_post_form
    data["post"] = False
    if request.method == "POST" and new_post_form.validate_on_submit():
        main_image = new_post_form.main_image.data
        title = new_post_form.title.data
        content = new_post_form.content.data
        url_title = "-".join(title.split(" "))
        description = new_post_form.description.data

        post = Post.query.filter(Post.url_title == url_title).first()
        
        # There is already a post, update it
        if post:
            print("Updating post", url_title)
            _new_post = False
        #New post
        else:
            print("Adding post", url_title)
            post = Post()
            _new_post = True

        post.main_image = main_image
        post.title = title
        post.url_title = url_title
        post.content = content
        post.description = description
        

        data["post"] = post

        if _new_post:
            db.sessison.add(post)
        db.session.commit()

    if post_to_edit:
        post = Post.query.filter(Post.url_title == post_to_edit).first()
        data["post"] = post
    # Get all posts that are in db
    posts = Post.query.all()
    data["posts"] = posts
    return render_template("templates/new_post.html", data=data)




@app.route('/register' , methods=['GET','POST'])
def register():
    data = Base()
    signup_form = Signup_form(prefix="signup")
    data["forms"]["signup_form"] = signup_form

    if signup_form.validate_on_submit():

        username = signup_form.username.data
        password = signup_form.password.data
        email = signup_form.email.data
        first_name = signup_form.first_name.data
        last_name = signup_form.last_name.data

        user = User(username, password, email)
        user.first_name = first_name
        user.last_name = last_name

        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('profile'))
    else:
        return render_template('templates/register.html', data=data)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/login',methods=['GET','POST'])
def login():
    login_form = Login_form(prefix="login")
    data = Base()
    data["forms"]["login_form"] = login_form
    if login_form.validate_on_submit():

        username = login_form.username.data
        password = login_form.password.data

        registered_user = User.query.filter_by(username=username).first()
        if registered_user is None:
            flash("username is incorrect", "errorMsg")
        else:
            if registered_user.verify_password(password):
                login_user(registered_user)
                return redirect(request.args.get('next') or url_for('profile'))
            else:
                flash("password is incorrect", "errorMsg")
    
    return render_template('templates/login.html', data=data)

#Main menu stuff
@app.route("/performance", methods=["GET"])
def performance():
    return render_template("templates/performance")



@app.route("/faq", methods=["GET"])
def faq():
    return render_template("templates/faq")

#Profile menu stuff
@app.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/profile/privacy')
@login_required
def privacy():
    if request.method == "GET":
        return render_template("templates/privacy.html")
        
@app.route('/api/deletePersonalData', methods=["POST"])
@login_required
def delete_personal_data():
    json = request.get_json()
    response = Response()
    try:
        model_attr = json["model_attr"]
    except KeyError:
        response.msg = "could not find key 'model_attr'"
        return response.send()

    changed = False
    if model_attr == "email":
        g.user.email = None
        changed = True;

    elif model_attr == "first_name":
        g.user.first_name = None
        changed = True;

    elif model_attr == "last_name":
        g.user.last_name = None
        changed = True;
    
    elif model_attr == "registered_on":
        g.user.registered_on = None
        changed = True;

    if changed:
        db.session.commit()
        return response.send(success=True)
    else:
        response.msg = "could not find model attribute '" + model_attr + "'"
        return response.send()

@app.route('/contact', methods=["GET", "POST"])
def contact():
    data = Base()
    contact_form = Contact_form()
    data["forms"]["contact_form"] = contact_form
    if contact_form.validate_on_submit():
        message = contact_form.message.data
        from_email = contact_form.email.data
        header = "Visitor contact request"
        if(g.logged_in):
            header = "User contact request"
        
        send_mail_async(header, message, to_email="info@bitbotly.com", from_email=from_email)
        flash("Message sent. We'll respond as quick as possible", "infoMsg")
    return render_template("templates/contact.html", data=data)




@app.route('/profile')
@login_required
def profile():
    return render_template("templates/profile.html")