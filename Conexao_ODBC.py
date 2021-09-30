import teradata as td
from teradata import tdodbc

def conectar():
    
    udaExec = td.UdaExec(appName="HelloWorld", version="1.0", logConsole=False)
    session = udaExec.connect(method="ODBC", driver='Teradata Database ODBC Driver 16.20', dsn="TeraDriver", username='YOURUSER', 
    password= 'YOURPASSWORD')
    return session

