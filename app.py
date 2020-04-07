from flask import Flask, jsonify

app = Flask(__name__)

desenvolvedores = [
    {
        'nome': 'Wesley Pires',
        'habilidades': ['Python', 'Flask']
    },
    {
        'nome': 'Rafael Cordas',
        'habilidades': ['Javascript', 'HTML']
    },
    {
        'nome': 'Ana Silva',
        'habilidades': ['PHP', 'HTML', 'CSS']
    }
]

@app.route('/dev')
def desenvolvedor():
    desenvolvedor = desenvolvedores
    return jsonify(desenvolvedor)

if __name__ == "__main__":
    app.run(debug=True)