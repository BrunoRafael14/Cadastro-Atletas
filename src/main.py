from flask import Flask
from blueprints.login import login_bp
from blueprints.cadastro_atleta import cadastro_atleta_bp

app = Flask(__name__)

app.register_blueprint(login_bp, url_prefix='/')

app.register_blueprint(cadastro_atleta_bp, url_prefix='/cadastro_atleta')

if __name__ == "__main__":
    app.run(debug=True)