from flask import Blueprint, render_template
from blogger.post.models import Post

page = Blueprint('page', __name__)


@page.route('/', defaults={'page': 1})
@page.route('/page/<int:page>')
def home(page):
    posts = Post.query.order_by(Post.created_on.desc()).paginate(page=page, per_page=10)
    return render_template('page/home.html', posts=posts)
