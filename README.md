# Consumindo API e salvando em modelo

Este projeto consome os dados de uma API e salva esses dados em uma aplicação Django

[![Build Status](https://travis-ci.org/eltonjncorreia/jobs.svg?branch=master)](https://travis-ci.org/eltonjncorreia/jobs)
[![Code Health](https://landscape.io/github/eltonjncorreia/jobs/master/landscape.svg?style=flat)](https://landscape.io/github/eltonjncorreia/jobs/master)

## Como Usar?

1.  Clone o repositório.
2.  Crie um virtualenv com Python 3.6 +
3.  Ative o virtualenv
4.  Instale as dependências.
5.  Configure a instância com o .env
6.  Rode os testes
7.  Execute o projeto.


``` console
git clone https://github.com/eltonjncorreia/jobs.git ello
cd ello
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
python manage.py runserver

```