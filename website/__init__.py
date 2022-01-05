from flask import Flask

def create_app():
    app = Flask(__name__) # name of the file that was ran
    secret_key = "this is a test secret key avocado" #encrypted cookies #TODO: remove reference for the secret key from the source code
    app.config["SECRET_KEY"] = secret_key

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return(app)

