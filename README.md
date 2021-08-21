# API REST para controle de produtos

Esta é uma simples API REST que contém listagem , cadastro , edição e deleção das entidades abaixo:

    - Descrição
    - Quantidade 
    - Descrição 

## Requisitos para a Instalação

1. Flask

    pip install flask

2. Flask-sqlalchemy

    pip install flask-sqlalchemy

## Banco MySQL

1. Caso já tenha o banco e queira criar as tabelas, abra o arquivo "criar_tabelas.py", coloque os dados do banco, salve e execute o "banco_produtos.py" e altere os dados de conexão no "produtos.py", após execute a sequência.
    
    python criar_banco_produtos.py

    python produtos.py

## acessando a API


    para acessar a API  no terminal digite:

        $ python produtos.py


    1. Listar os produtos cadastrados

        http://localhost:5000/


    2. cadastrar produtos

        curl -X POST  -d "descricao=DESCRICAO&quantidade=QUANTIDADE&valor=VALOR" http://localhost:5000/cadastro


    3. editar dados de um produto

        curl -X PUT -d "descricao=DESCRICAO&quantidade=QUANTIDADE&valor=VALOR" http://localhost:5000/editar/<id>


    4. Deletar um registro de produto
 
        curl -X DELETE -d "descricao=DESCRICAO&quantidade=QUANTIDADE&valor=VALOR" http://localhost:5000/apagar/<id>


    5. Pesquisar um produto pela descrição

        http://localhost:5000/filtro/<descricao>

