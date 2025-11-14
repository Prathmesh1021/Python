import pyodbc

DRIVER_NAME = "SQL Server"
SERVER_NAME = "DESKTOP-10Q22E\\SQLEXPRESS01"
DATABASE_NAME = "MyDB"

connection_string = f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trusted_Connection=yes;
"""

conn = pyodbc.connect(connection_string)
print("Connected successfully:", conn)
