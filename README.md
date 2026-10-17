# Gerador de Senhas

Aplicação web que gera senhas aleatórias e seguras. O usuário escolhe o tamanho da senha e recebe o resultado na hora, direto na página.

## Funcionalidades

- Escolha do tamanho da senha (de 4 a 120 caracteres)
- Cada senha tem pelo menos 1 letra minúscula, 1 maiúscula, 1 número e 1 símbolo
- Caracteres embaralhados no final, para a ordem não ser previsível
- Validação no navegador (HTML) e também no servidor (Flask)
- Mensagens de erro para tamanho inválido ou campo vazio

## Tecnologias

- Python 3
- Flask
- HTML e CSS
- Módulo `secrets` do Python, indicado para senhas por usar uma fonte de aleatoriedade segura (diferente do `random`)

## Como rodar

1. Clone o repositório e entre na pasta do projeto:

```
git clone https://github.com/victorgasparotti/gerador-de-senhas.git
cd gerador-de-senhas
```

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Rode a aplicação:

```
python app.py
```

4. Abra no navegador: http://127.0.0.1:5000

## Estrutura do projeto

```
gerador-de-senhas/
├── app.py              # rotas do Flask e função que gera a senha
├── templates/
│   └── pagina.html     # página com o formulário
├── static/
│   └── style.css       # estilos da página
├── requirements.txt    # dependências
└── README.md
```

## Autor

Victor Gasparotti, [github.com/victorgasparotti](https://github.com/victorgasparotti)