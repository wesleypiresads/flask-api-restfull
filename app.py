from flask import Flask, jsonify, request, json

app = Flask(__name__)

produtos = [
    {
        'id': 0,
        'marca': 'Samsung',
        'modelo': 'J5 Prime',
        'preco': 380.00
    },
    {
        'id': 1,
        'marca': 'Motorola',
        'modelo': 'Moto G4',
        'preco': 300.00
    }
]

# Método GET para exibir todos os produtos
@app.route('/')
def index():
    return jsonify(produtos)

# Método GET com id para exibir um produto específico
@app.route('/produto/<int:id>/', methods=['GET'])
def produto(id):
    if request.method == 'GET':
        try:
            response = produtos[id]
        except IndexError:
            response = {'mensagem': 'Nao existe o produto com o codigo: {}'.format(id)}
        return jsonify(response)

# Método POST para adicionar um produto
@app.route('/produto/', methods=['POST'])
def InsertProduto():
    if request.method == 'POST':
        getProduto = json.loads(request.data)
        idProduto = len(produtos)
        getProduto['id'] = idProduto
        produtos.append(getProduto)
        return jsonify(getProduto)

# Método PUT para alterar um produto
@app.route('/produto/<int:id>/', methods=['PUT'])
def UpdateProduto(id):
    if request.method == 'PUT':
        getProduto = json.loads(request.data)
        produtos[id] = getProduto
        return jsonify(getProduto)

# Método DELETE para excluir um produto
@app.route('/produto/<int:id>/', methods=['DELETE'])
def DelProduto(id):
    if request.method == 'DELETE':
        produtos.pop(id)
        response = {'mensagem': 'O produto de codigo: {} foi excluído'.format(id)}
        return jsonify(response)


# Start o servidor com debug ativa para ambiente de desenvolvimento
if __name__ == "__main__":
    app.run(debug=True)