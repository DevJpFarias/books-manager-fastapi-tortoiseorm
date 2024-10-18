## Projeto para base de estudos com FastAPI (Python)

1. Iremos criar uma pasta de virtualEnv (venv) para evitar ficar instalando dependências no computador.
```bash
$ python3 -m venv venv
```

2. Para entrar no venv, basta usar o seguinte comando:
```bash
$ source venv/bin/activate
```

3. Instalar as dependências
```bash
$ pip install -r requirements.txt
```

*. Caso não tenha o arquivo, crie com as dependências atuais com o comando:
```bash
$ pip freeze > requirements.txt
```

*. Para parar o ambiente virtual
```bash
$ deactivate
```

*. Para verificar as dependências
```bash
$ pip freeze
```