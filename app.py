from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

ranking = []

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/ranking', methods=['GET'])
def get_ranking():
    return jsonify(ranking)

@app.route('/atualizar', methods=['POST'])
def atualizar_ranking():
    data = request.json
    nome = data.get('nome')
    pontos = data.get('pontos')
    ranking.append((pontos, nome))
    ranking.sort(reverse=True, key=lambda x: x[0]) 
    return jsonify({"status": "sucesso", "ranking": ranking})

if __name__ == '__main__':
    app.run(debug=True)
