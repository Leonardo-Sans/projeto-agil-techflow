# tests/test_app.py

import sys
import os

# Adiciona o diretório 'src' ao path para que possamos importar 'app'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from app import app

@pytest.fixture
def client():
    """Cria um cliente de teste para a aplicação Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_pagina_principal(client):
    """Testa se a página principal carrega corretamente."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Gerenciador de Tarefas" in response.data

def test_criar_tarefa(client):
    """Testa a criação de uma nova tarefa."""
    client.post('/criar', data={'titulo': 'Tarefa Teste', 'descricao': 'Descricao Teste'})
    response = client.get('/')
    assert b"Tarefa Teste" in response.data