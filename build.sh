# Instalar el controlador ODBC para SQL Server en Debian/Ubuntu
sudo su
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
exit

sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17


#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate