from flask import Flask


def create_app():
    app = Flask(__name__)

    # creates our secret code
    app.config["SECRET_KEY"] = "dogs"

    from .views import views
    # from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    # app.register_blueprint(auth, url_prefix ='/auth')
    # TODO seperate the things out of the views into welcome, login, quiz, etc

    return app
