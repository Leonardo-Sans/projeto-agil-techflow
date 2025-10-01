# Projeto Ágil com GitHub: Sistema de Gerenciamento de Tarefas

Este projeto simula o desenvolvimento de um sistema de gerenciamento de tarefas para a empresa fictícia TechFlow Solutions, aplicando conceitos de Engenharia de Software e metodologias ágeis.

## 🎯 Objetivo e Escopo

O objetivo é criar um sistema web simples (CRUD) que permita aos usuários criar, visualizar e excluir tarefas. O projeto serve como uma demonstração prática do uso do GitHub para gestão de projetos, controle de versão, qualidade e mudanças.

## 🚀 Metodologia Adotada

Foi utilizada a metodologia ágil **Kanban** para a gestão das tarefas, aproveitando a ferramenta **GitHub Projects**. O quadro é dividido nas colunas "A Fazer", "Em Progresso" e "Concluído", permitindo um acompanhamento visual e contínuo do fluxo de trabalho.

## 📋 Requisitos e Modelagem UML

### Requisitos Funcionais
- **RF01:** O sistema deve permitir a criação de uma nova tarefa com título e descrição.
- **RF02:** O sistema deve permitir a visualização de todas as tarefas cadastradas.
- **RF03:** O sistema deve permitir a exclusão de uma tarefa.

### Requisitos Não Funcionais
- **RNF01:** O sistema deve ser desenvolvido em Python com Flask.
- **RNF02:** A interface deve ser simples e baseada em HTML.
- **RNF03:** O código deve possuir testes unitários automatizados via GitHub Actions.

### Modelagem UML

**Diagrama de Casos de Uso**

graph TD
    A[Usuário] --> B(Criar Tarefa)
    A --> C(Visualizar Tarefas)
    A --> D(Excluir Tarefa)

    style A fill:#fff,stroke:#333,stroke-width:2px,actor


**Diagrama de Classes**

classDiagram
    class Tarefa {
        +int id
        +string titulo
        +string descricao
    }


## 🛠️ Instruções para Execução do Sistema

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/projeto-agil-techflow.git](https://github.com/SEU_USUARIO/projeto-agil-techflow.git)
    cd projeto-agil-techflow
    ```
2.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows: venv\Scripts\activate
    # Linux/Mac: source venv/bin/activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute a aplicação:**
    ```bash
    python src/app.py
    ```
5.  Acesse `http://127.0.0.1:5000` no seu navegador.

## 🔄 Gestão de Mudanças: Simulação de Mudança de Escopo

Durante o desenvolvimento, o cliente solicitou uma nova funcionalidade para adicionar um nível de **prioridade** ("Baixa", "Média", "Alta") a cada tarefa.

**Justificativa:** A inclusão de prioridades é essencial para a equipe de logística do cliente, permitindo que eles foquem nas tarefas mais críticas e otimizem o fluxo de trabalho.

**Impacto e Ação:**
- A tarefa "Implementar campo de prioridade nas tarefas" foi adicionada ao backlog no quadro Kanban.
- O modelo de dados da `Tarefa` precisará ser atualizado para incluir o novo atributo.
- A interface de criação e visualização de tarefas será modificada para exibir o campo de prioridade.

---

Projeto desenvolvido para a disciplina de Engenharia de Software.

