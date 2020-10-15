import pyodbc
server = 'Localhost'
database = 'AdventureWorks'
username = 'sa'
password = '********'   
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("Select * From Production.Location")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
