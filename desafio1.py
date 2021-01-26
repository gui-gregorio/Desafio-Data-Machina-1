from flask import Flask, request, jsonify

app = Flask(__name__)


# Função para calcular o termo desejado da sequência
def fibonacci(n):
    if n <= 1:
        return n
    else:
        n = fibonacci(n - 1) + fibonacci(n - 2)
        return n


# Execução da API:
@app.route('/', methods=['POST'])
def home():
    resultado = request.json["resultado"]  # aceita o request de um valor para poder fazer o cálculo
    n1 = fibonacci(int(resultado))  # Converte o input para INT e faz o cálculo
    return jsonify(n1)  #retorna o resultado
