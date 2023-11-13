# Instalar el controlador ODBC para SQL Server en Debian/Ubuntu (sin sudo)
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > mssql-release.list
mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
mv mssql-release.list /etc/apt/sources.list.d/mssql-release.list

# Actualizar el índice del paquete y luego instalar el controlador ODBC (sin sudo)
apt-get update
apt-get install -y msodbcsql17

#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate