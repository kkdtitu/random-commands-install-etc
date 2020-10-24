import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

#Sample 4 values for server, database, username, password are:
server = 'tcp:myserver.database.windows.net' 
database = 'mydb' 
username = 'myusername' 
password = 'mypassword' 

#Actual 4 values for server, database, username, password are:
# 'tcp:isye-6420-project.database.windows.net,1433' 
# 'topic_modelling' 
# 'project_administrator' 
# 'isye_6420_admin'
 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()