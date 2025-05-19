# ToDo-App Django

Aplicação web para gerenciamento de tarefas feita com Django 5.x.

## Funcionalidades

- Cadastro, edição e exclusão de tarefas  
- Organização por categorias e prioridades  
- Filtros por status (pendente, em andamento, concluída)  
- Dashboard com estatísticas básicas  
- Sistema de autenticação de usuários (login/logout)  
- Interface responsiva com Bootstrap  

## Tecnologias

- Python 3.x  
- Django 5.x  
- SQLite (banco de dados)  
- HTML, CSS (Bootstrap)  
- JavaScript básico  

## Como rodar o projeto

1. Clone o repositório  
   bash
   git clone https://github.com/seu-usuario/todo-app-django.git
   cd todo-app-django
2. Crie um ambiente Virtual e ative:
   Linux/macOS:

      python3 -m venv venv
      source venv/bin/activate

   Windows:
      python -m venv venv
      venv\Scripts\activate
   
3. Instale as dependências:

   pip install -r requirements.txt

4. Rode as Migrations:

   python manage.py migrate

5. Inicie o servidor:

   python manage.py runserver

6. Acesse http://127.0.0.1:8000 no navegador

## Próximos passos
- Implementar notificações

- Melhorar o dashboard com gráficos

- Fazer deploy em servidor real