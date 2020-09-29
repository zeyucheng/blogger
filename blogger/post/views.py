from flask import render_template, url_for, flash, redirect, Blueprint, abort
from flask_login import current_user, login_required
from blogger.app import db, photos
from blogger.post.forms import PostForm
from blogger.post.models import Post

post_page = Blueprint('post_page', __name__)


@post_page.route('/post/new', methods=['GET', 'POST'])
@login_required
def new():
    form = PostForm()
    if form.validate_on_submit():
        post = Post()
        form.populate_obj(post)
        post.user_id = current_user.id

        if form.design_photo.data:
            design_photos = photos.save(form.design_photo.data)
            post.design_photo = design_photos
            db.session.add(post)
            db.session.commit()
            flash('New post has been created!', 'success')
        else:
            flash('Please Upload a Photo', 'danger')

        return redirect(url_for('page.home'))
    return render_template('post/new.html', form=form)


@post_page.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)
    form = PostForm(obj=post)

    if form.validate_on_submit():
        form.populate_obj(post)
        db.session.commit()
        flash('Post has been updated', 'success')
        return redirect(url_for('user_page.user_post', user_id=post.user.id))
    return render_template('post/edit.html', form=form)


@post_page.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()

    flash('Post has been delete', 'success')
    return redirect(url_for('user_page.user_post', user_id=post.user.id))
