# Casamento Back-end
### Tecnologias utilizadas:

[<img alt="Python" height="60" src="https://www.python.org/static/community_logos/python-logo-generic.svg" width="237"/>](https://www.python.org/)
[<img alt="Django" height="60" src="https://static.djangoproject.com/img/logos/django-logo-negative.svg" width="237"/>](https://www.djangoproject.com/)
[<img alt="Swagger" height="60" src="https://static1.smartbear.co/swagger/media/assets/images/swagger_logo.svg" width="237"/>](https://swagger.io/tools/swagger-editor/)
[<img alt="PostgreSQL" height="65" src="https://cdn.iconscout.com/icon/free/png-512/postgresql-11-1175122.png" width="65"/>](https://www.postgresql.org)

### Dependências do sistema:

Para realizar o deploy do servidor é necessário seguir os passos:

- Instalar o Python na versão 3.10.
- Instalar as dependências do projeto pelo PyPI do Python: 
	- pip install -r requirements.txt
- Instalar o PostgreSQL e criar um banco com o nome "casamento".

Observação: Se a sua máquna possuir a versão 2.7 do Python instalada ou qualquer outra versão, será necessário substituir o comando (pip install "nome_da_dependência") por (pip3 install "nome_da_dependência") ou (pip3.10 install "nome_da_dependência").

### Deploy do servidor:

Para realizar o deploy do servidor é necessário seguir os passos:
 - Abrir o arquivo settings.py na pasta casamento.
 - Ir até o JSON de configuração "DATABASES" e configurar o usuário, senha e host do banco de dados.
 - Abrir um CMD Windows ou Terminal Linux na pasta raiz do projeto (onde se encontra o arquivo manage.py).
 - Executar a migração do banco de dados com o comando a seguir:
	 -  python3.10 manage.py migrate
- Executar o comando para realizar o deploy do servidor:
	- python3.10 manage.py runserver

### Acessar o Swagger

Para acessar o Swagger basta abrir o navegador e acessar o link: http://127.0.0.1:8000/swagger/.

### Configuração Heroku para staticfiles

Acessar: "Heroku > my_app > settings > config vars" e inserir a variável: DISABLE_COLLECTSTATIC=1.
