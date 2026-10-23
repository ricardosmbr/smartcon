# Sistema de clientes para smart contract em Python
https://smartconbr.herokuapp.com/
com Django e Azure SQL
## Pré-requisitos do sistema
- [Git](https://git-scm.com)
- Python 3.12.11
- Virtualenv
- Django 5.2 LTS (installed from `requirements.txt`)
- Microsoft ODBC Driver 18 for SQL Server e unixODBC no Linux. Consulte a
  [documentação de instalação da Microsoft](https://learn.microsoft.com/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server)

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
Configure `SECRET_KEY`, `WEB3_PROVIDER_URL` e `WEB3_CHAIN_ID` no ambiente antes de iniciar o sistema. Para Ethereum Sepolia, use um RPC Sepolia e o chain ID `11155111`. Para conectar ao Azure SQL, configure `DB_PASSWORD`; `DB_NAME`, `DB_USER`, `DB_HOST` e `DB_PORT` podem ser definidos para substituir os padrões. Nunca inclua a senha no código ou em arquivos versionados. As configurações de e-mail (`EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` e `EMAIL_PORT`) são opcionais.
## baixe o projeto
