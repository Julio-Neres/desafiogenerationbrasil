from flasgger import Swagger
from flasgger.utils import swag_from
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@postgres:5432/escola'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STATIC_FOLDER'] = 'static'

db = SQLAlchemy(app)
swagger = Swagger(app)

app.config['SWAGGER'] = {
    'title': 'Documentação da API',
    'uiversion': 3
}

class Alunos(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    idade = db.Column(db.Integer)
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    nome_professor = db.Column(db.String(255))
    numero_sala = db.Column(db.String(10))

# Documente a rota '/'
@app.route('/')
@swag_from('swagger_config/listar_alunos.yml')
def listar_alunos():
    """
    Lista de Alunos
    ---
    responses:
      200:
        description: Lista de todos os alunos
    """
    alunos = Alunos.query.all()
    return render_template('listar_alunos.html', alunos=alunos)

# Documente a rota '/adicionar_aluno'
@app.route('/adicionar_aluno', methods=['GET', 'POST'])
@swag_from('swagger_config/adicionar_aluno.yml')
def adicionar_aluno():
    """
    Adicionar Aluno
    ---
    responses:
      200:
        description: Aluno adicionado com sucesso
    """
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        nota_primeiro_semestre = request.form['nota_primeiro_semestre']
        nota_segundo_semestre = request.form['nota_segundo_semestre']
        nome_professor = request.form['nome_professor']
        numero_sala = request.form['numero_sala']

        aluno = Alunos(nome=nome, idade=idade, nota_primeiro_semestre=nota_primeiro_semestre, nota_segundo_semestre=nota_segundo_semestre, nome_professor=nome_professor, numero_sala=numero_sala)

        db.session.add(aluno)
        db.session.commit()

        return redirect(url_for('listar_alunos'))

    return render_template('adicionar_aluno.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
