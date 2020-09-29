from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from blogger.user.models import User
from blogger.post.models import Post
from blogger.request.models import Request
from blogger.app import db, bcrypt, photos
from blogger.user.forms import SignUpForm, LoginForm, UpdateProfileForm

user_page = Blueprint('user_page', __name__)


@user_page.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.session.add(user)
        db.session.commit()
        flash('Thanks for sign up', 'success')

        return redirect(url_for('user_page.login'))

    return render_template('user/signup.html', form=form)


@user_page.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('page.home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('page.home'))
        else:
            flash('your email or password was entered incorrectly.', 'danger')

    return render_template('user/login.html', form=form)


@user_page.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('page.home'))


@user_page.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm(obj=current_user)
    if form.validate_on_submit():
        form.populate_obj(current_user)

        if form.image.data:
            profile_image = photos.save(form.image.data)
            current_user.profile_image = profile_image
        db.session.commit()

        flash('Your profile has been updated', 'success')
        return redirect(url_for('user_page.profile'))

    return render_template('user/profile.html', form=form)


@user_page.route('/user/id=<int:user_id>/page/<int:page>', defaults={'page': 1})
@user_page.route('/user/id=<int:user_id>/page/<int:page>')
def user_post(user_id, page):
    user = User.query.filter_by(id=user_id).first_or_404()
    posts = Post.query.filter_by(user_id=user.id).order_by(Post.created_on.desc()).paginate(page=page, per_page=10)

    return render_template('user/posts.html', posts=posts, user=user)



def user_order(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    return render_template('user/posts.html', user=user)

