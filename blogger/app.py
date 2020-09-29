from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'user_page.login'
login_manager.login_message = 'Please log in to access this page'
login_manager.login_message_category = 'danger'

photos = UploadSet('photos', IMAGES)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    configure_uploads(app, photos)

    from blogger.page.views import page
    from blogger.user.views import user_page
    from blogger.post.views import post_page
    from blogger.request.views import request_page
    app.register_blueprint(page)
    app.register_blueprint(user_page)
    app.register_blueprint(post_page)
    app.register_blueprint(request_page)

    return app