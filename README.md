# Oystr-CodeTest-Services

Teste encomendado pelo pessoal da Oystr – Robôs de automação.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.9.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone git@github.com:niltonpimentel02/oystr.git oystr
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
crie um novo webhook em https://webhook.site/
coloque a url do webhook na variável de ambiente WEBHOOK_SITE=
```

## Rodar projeto

```console
export FLASK_APP=app
flask run
```

## Rotas

O `POST` deve ser feito para: ` http://127.0.0.1:5000/notification`

## Insomnia test

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Run%20in%20Insomnia&uri=https%3A%2F%2Fraw.githubusercontent.com%2Fniltonpimentel02%2Foystr%2Fmain%2Finsomnia.json)

## Pytest
Para gerar o relatório de cobertura do código abaixo: `pytest -v --cov=oystr tests/`

```console
----------- coverage: platform linux, python 3.9.0-final-0 -----------
Name                   Stmts   Miss     Cover
---------------------------------------------
execution_process.py      21      0   100.00%
---------------------------------------------
TOTAL                     21      0   100.00%
```
