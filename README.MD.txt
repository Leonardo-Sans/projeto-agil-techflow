```mermaid
graph TD
    A[Usuário] --> B(Criar Tarefa)
    A --> C(Visualizar Tarefas)
    A --> D(Excluir Tarefa)

    style A fill:#fff,stroke:#333,stroke-width:2px,actor

```mermaid
classDiagram
    class Tarefa {
        +int id
        +string titulo
        +string descricao
    }