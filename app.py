from flask import Flask, render_template, request
import string
import secrets


minusculas = string.ascii_lowercase
maiusculas = string.ascii_uppercase
numeros = string.digits
simbolos = '!@#$'

def gerar_senha(tamanho):
    senha = secrets.choice(minusculas) + secrets.choice(maiusculas) + secrets.choice(numeros) + secrets.choice(simbolos)

    todos_os_caracteres = minusculas + maiusculas + numeros + simbolos

    for i in range(tamanho - 4):
        senha += secrets.choice(todos_os_caracteres)

    lista = list(senha)
    secrets.SystemRandom().shuffle(lista)
    senha = ''.join(lista)

    return senha

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        quantidade = int(request.form['tamanho'])
        if quantidade < 4:
            return render_template('pagina.html', erro='A senha precisa ter no minimo 4 caracteres.')
        if quantidade < 4 or quantidade > 120:
            return render_template('pagina.html', erro='A senha precisa ter entre 0 e 120.')
        return render_template('pagina.html', senha = gerar_senha(quantidade))
    return render_template("pagina.html")


if __name__ == '__main__':
    app.run(debug=True)