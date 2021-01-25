from flask import Flask, request

app = Flask(__name__)


# Função para calcular o termo desejado da sequência
def fibonacci(n):
    if n <= 1:
        return n
    else:
        n = fibonacci(n - 1) + fibonacci(n - 2)
        return n


# Execução da API:
@app.route('/', methods=['GET'])
def home():
    resultado = request.json["fibonacci"]  # aceita o request de um valor para poder fazer o cálculo
    n1 = fibonacci(int(resultado))  # Converte o input para INT e faz o cálculo
    n2 = str(n1)  # converte o resultado novamente para STR, para que possa retornar na API
    return n2
