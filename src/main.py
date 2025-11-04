from flask import Flask
from blueprints.login import login_bp

app = Flask(__name__)

app.register_blueprint(login_bp, url_prefix='/')

if __name__ == "__main__":
    app.run(debug=True)