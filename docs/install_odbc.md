### How to use pyodbc to access SQL Server

1. Install Driver from Microsoft[https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15#ubuntu17] (Based on what system do you operate)
``` 
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

apt-get update

ACCEPT_EULA=Y apt-get install msodbcsql17
ACCEPT_EULA=Y apt-get install msodbcsql=13.0.1.0-1 mssql-tools=14.0.2.0-1

sudo apt-get install unixodbc-dev-utf16
apt-get install unixodbc-dev
apt-get install libodbc1

# Create Symbolic link
ln -sfn /opt/mssql-tools/bin/sqlcmd-13.0.1.0 /usr/bin/sqlcmd
ln -sfn /opt/mssql-tools/bin/bcp-13.0.1.0 /usr/bin/bcp
```

2 Install ODBC Python Library  
``` 
pip install pyodbc 
```
