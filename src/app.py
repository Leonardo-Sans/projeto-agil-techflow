# src/app.py

from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Usando um dicionário em memória para simular um banco de dados
# A chave será o ID da tarefa
tarefas_db = {}
next_id = 1

# Template HTML em uma string para simplicidade
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>TechFlow - Gerenciador de Tarefas</title>
    <style>
        body { font-family: sans-serif; margin: 2em; }
        .tarefa { border: 1px solid #ccc; padding: 10px; margin-bottom: 10px; border-radius: 5px; }
        .tarefa form { display: inline; }
    </style>
</head>
<body>
    <h1>Gerenciador de Tarefas - TechFlow Solutions</h1>

    <h2>Adicionar Nova Tarefa</h2>
    <form action="{{ url_for('criar_tarefa') }}" method="post">
        <input type="text" name="titulo" placeholder="Título da Tarefa" required>
        <input type="text" name="descricao" placeholder="Descrição">
        <button type="submit">Adicionar</button>
    </form>

    <h2>Tarefas a Fazer</h2>
    {% for id, tarefa in tarefas.items() %}
        <div class="tarefa">
            <strong>{{ tarefa.titulo }}</strong>
            <p>{{ tarefa.descricao }}</p>
            <form action="{{ url_for('excluir_tarefa', tarefa_id=id) }}" method="post">
                <button type="submit">Excluir</button>
            </form>
        </div>
    {% else %}
        <p>Nenhuma tarefa ainda!</p>
    {% endfor %}
</body>
</html>
"""

@app.route('/')
def listar_tarefas():
    """ Rota principal que exibe todas as tarefas. """
    # Ordena as tarefas pelo ID antes de renderizar
    tarefas_ordenadas = dict(sorted(tarefas_db.items()))
    return render_template_string(HTML_TEMPLATE, tarefas=tarefas_ordenadas)

@app.route('/criar', methods=['POST'])
def criar_tarefa():
    """ Rota para criar uma nova tarefa. """
    global next_id
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')

    if titulo:
        tarefas_db[next_id] = {'titulo': titulo, 'descricao': descricao}
        next_id += 1

    return redirect(url_for('listar_tarefas'))

@app.route('/excluir/<int:tarefa_id>', methods=['POST'])
def excluir_tarefa(tarefa_id):
    """ Rota para excluir uma tarefa. """
    if tarefa_id in tarefas_db:
        del tarefas_db[tarefa_id]

    return redirect(url_for('listar_tarefas'))

# Roda a aplicação
if __name__ == '__main__':
    app.run(debug=True)