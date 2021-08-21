## esta operação não é necessária caso seja utilizado o banco configurado


# importando os frameworks necessários

from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

# os itens URL_CONEXÃO, PORTA, USUÁRIO, SENHA e NOME_DO_BANCO, 
# devem ser configurados para o servidor MySQL desejado
# caso alguma tabela já exista no banco então é retornado o código 404

app.config['MYSQL_DATABASE_HOST'] = 'HOST'
app.config['MYSQL_DATABASE_PORT'] = PORTA
app.config['MYSQL_DATABASE_USER'] = 'USUARIO'
app.config['MYSQL_DATABASE_PASSWORD'] = 'SEBGA'
app.config['MYSQL_DATABASE_DB'] = 'BANCO'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8'


# estabelecendo a conexão com o banco

mysql = MySQL()
mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()



# definindo variável que recebe o query para criar a tabela de produtos no banco escolhido

try:
	sql_produtos = "CREATE TABLE produtos(id INT NOT NULL AUTO_INCREMENT, descricao VARCHAR(150), quantidade INT, valor INT)"
except Exception:
	jsonify({'status_code':404})


# executando os QUERYs de criação das tabelas no banco

cursor.execute(sql_produtos)


# fechando a conexão com o banco

conn.close()


# rodando o flask
app.run()