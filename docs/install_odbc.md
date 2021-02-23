### How to use pyodbc to access SQL Server

1. [Install Driver from Microsoft](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15#ubuntu17) (Based on what system do you operate)
``` 
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

apt-get update

ACCEPT_EULA=Y apt-get install msodbcsql17
ACCEPT_EULA=Y apt-get install mssql-tools

apt-get install unixodbc-dev


echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc
```

2 Install ODBC Python Library  
``` 
pip install pyodbc 
```
