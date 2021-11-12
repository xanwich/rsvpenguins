from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"


@app.template_filter()
def format_int(i):
    return f"{i:,}"


from routes import *  # NOQA

if __name__ == "__main__":

    app.logger.critical("start")
    app.run(debug=False)
