from flask import Blueprint, render_template, request
from services.salvar_dados import salvar_dados

cadastro_atleta_bp = Blueprint('cadastro_atleta', __name__, template_folder='templates/cadastro_atleta', static_folder='static/cadastro_atleta')

@cadastro_atleta_bp.route("/", methods=['GET', 'POST'])
def cadastro_atleta():
    if request.method == 'POST':
        nome_atleta=request.form.get('nome_atleta')
        idade=request.form.get('idade')
        posicao=request.form.get('posicao')
        dados_atleta = {
            'nome_atleta': nome_atleta,
            'idade': idade,
            'posicao': posicao
        }

        salvar_dados(dados_atleta)

        return render_template("cadastro_atleta/cadastro_atleta.html", dados_atleta=dados_atleta)
    return render_template("cadastro_atleta/cadastro_atleta.html")

