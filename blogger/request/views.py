from flask import render_template, url_for, flash, redirect, Blueprint, abort
from flask_login import current_user, login_required
from blogger.app import db, photos
from blogger.user.models import User
from blogger.request.forms import RequestForm
from blogger.request.models import Request

request_page = Blueprint('request_page', __name__)


@request_page.route('/request/order', methods=['GET', 'POST'])
@login_required
def order(designer_id):
    form = RequestForm()
    if form.validate_on_submit():
        request = Request()
        form.populate_obj(request)
        request.user_id = current_user.id
        # request.designer_id =
        if form.user_photo.data:
            user_photos = photos.save(form.user_photo.data)
            request.user_photo = user_photos
            db.session.add(request)
            db.session.commit()
            flash('New order has been created!', 'success')
        else:
            flash('Please Upload a Photo', 'danger')

        return redirect(url_for(''
                                ''))
    return render_template('request/order.html', form=form)