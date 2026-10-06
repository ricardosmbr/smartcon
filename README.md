# Sistema de clientes para smart contract em Python
https://smartconbr.herokuapp.com/
com Django e Mysql(MariaDB)
## Pré-requisitos do sistema
- [Git](https://git-scm.com)
- Python 3.12.11
```

Para Linux debian 9.7 é necessário instalar antes
sudo apt-get install build-essential checkinstall python-dev python-setuptools python-pip python-smbus zlib1g-dev libffi-dev libncursesw5-dev libgdbm-dev libc6-dev libsqlite3-dev tk-dev libssl-dev openssl default-libmysqlclient-dev

```
```
Para Windows é necessário instalar antes
Visual studio >= 2014
```
- Virtualenv
- Django 5.2 LTS (installed from `requirements.txt`)
- Maria db 10.1

'''
sudo apt update && sudo apt install -y python3-dev default-libmysqlclient-dev build-essential pkg-config
'''

## Instalando o MariaDB
```
apt-get install mariadb-server
```

## Instalando o virtualenv
```
sudo pip install virtualenv
ou
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

```
## Criando o ambiente virtual
```
pyenv install 3.12.11
pyenv virtualenv 3.12.11 smart
pyenv activate smart
```
## Instalando as dependências
```
python -m pip install -r requirements-dev.txt
```
## Instalando o compilador Solidity usado pelo projeto
```
pip install solc-select
solc-select install 0.4.26

```
Configure `SECRET_KEY`, `WEB3_PROVIDER_URL` e `WEB3_CHAIN_ID` no ambiente antes de iniciar o sistema. Para Ethereum Sepolia, use um RPC Sepolia e o chain ID `11155111`. Para banco de dados, configure `DATABASE_URL`; as configurações de e-mail (`EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` e `EMAIL_PORT`) são opcionais.
## baixe o projeto
