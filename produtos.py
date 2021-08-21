"""
API REST para controle de estoque de produtos

Lista, cadastra, edita e deleta, em banco de dados MySQL, produtos,
retornando um arquivo JSON.

Este codigo e dividido nas partes listadas a seguir:
1. Lista produtos
2. Cadastra produtos
3. Edita produtos pelo id
4. Deleta produtos pelo id
5. Pesquisa produtos pelo nome
"""
from flask import Flask, jsonify, request, url_for, redirect, render_template
from flaskext.mysql import MySQL



app = Flask(__name__)


app.config['MYSQL_DATABASE_HOST'] = 'HOST'
app.config['MYSQL_DATABASE_PORT'] = PORTA
app.config['MYSQL_DATABASE_USER'] = 'USUARIO'
app.config['MYSQL_DATABASE_PASSWORD'] = 'SENHA'
app.config['MYSQL_DATABASE_DB'] = 'BANCO'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8'


mysql = MySQL()
mysql.init_app(app)


conn = mysql.connect()
cursor =conn.cursor()
  


@app.route('/', methods=['GET'])
def lista_prod():
    """
    Lista produtos cadastradas

    Popula uma lista com os dados contidos no banco e envia para um arquivo JSON. 
    """
    cursor.execute("SELECT * FROM produtos")
    novo = cursor.fetchall()
    lista = []
    for produtos in novo:
        lista.append('id: '+ str(produtos[0]))
        lista.append('descrição: '+ str(produtos[1]))
        lista.append('quantidade: '+ str(produtos[2]))
        lista.append('valor unitário: '+ str(produtos[3]))
    produtos = tuple(lista)
    return jsonify(produtos)



@app.route('/cadastro', methods=['POST'])
def insere_prod():
    """
    Insere novo produto no banco

    Recebe os valores de descrição, quantidade e valor unitário, verifica se os campos não está em branco
    autoincrementa o id retornando o codigo 201 se foi inserido com sucesso e o
    codigo 406 caso o nome esteja em branco. 
    O id é autoincrementado
    """
    try:                                    # verificando se foi passado o nome que e obrigatório
        descricao = request.form['descricao']
    except:
        return jsonify({'status_code':406}) # caso não seja passado o nome, retorna o codigo 406
    quantidade = request.form['quantidade']
    valor = request.form['valor']
    if descricao:
        cursor.execute("INSERT INTO produtos (descricao, quantidade, valor) \
        VALUES (%s, %s, %s)", (descricao, quantidade, valor)) # executa a query sql para insercao dos dados em um novo registro do banco
        cursor.connection.commit()
        return jsonify({'status_code':201})
        


@app.route('/editar/<int:id>', methods=['PUT'])
def edita_prod(id):
    """
    Edita os dados do produto

    Busca pelo id do produto o seu registro no banco, recebendo descrição, 
    quantidade e valor unitáriopara serem atualizados. Após o processo, 
    retorna o codigo 204.
    """
    descricao = request.form['descricao']
    quantidade = request.form['quantidade']
    valor = request.form['valor']
    cursor.execute("UPDATE produtos SET descricao = %s, quantidade = %d, valor = %d WHERE id = %s", (descricao, int(quantidade), int(valor), id))
    cursor.connection.commit()
    return jsonify({'status_code':204})



@app.route('/apagar/<int:id>', methods=['DELETE'])
def deleta_imob(id):
    """
    Apaga o registro de produto do banco

    Pelo id do produto e efetuada a delecao de seu registro no banco.

    """
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id))
    cursor.connection.commit()
    return jsonify({'status_code':200})



@app.route('/filtro/<descricao>', methods=['GET'])
def filtra_imob(descricao):
    """
    Filtra pela descrição do produto.

    Pela descriação do produto e feita a busca dos seus dados no banco e 
    retorna esses dados em um arquivo JSON.
    """
    cursor.execute("SELECT * FROM produtos WHERE descricao = %s", (str(descricao)))
    novo = cursor.fetchall()
    lista = []
    for produto in novo:
        lista.append('id: '+ str(produto[0]))
        lista.append('descricao: '+ str(produto[1]))
        lista.append('quantidade: '+ str(produto[2]))
        lista.append('valor unitário: '+ str(produto[3]))
    produtos = tuple(lista)
    return jsonify(produtos)


if __name__ == '__main__':
    app.run(debug=True)