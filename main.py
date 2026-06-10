from flask import Flask

# Inicializa a aplicação Flask
app = Flask(__name__)

# Define a rota para a página principal ("/")
@app.route("/")
def home():
    return "Olá, mundo! Esta é a minha primeira página com Flask."

@app.route("/contatos")
def contatos():
    return "Esta é a página de contatos."

# Inicia o servidor local
if __name__ == "__main__":
    app.run(debug=True)