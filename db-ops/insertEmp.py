import mysql.connector
import db_connector_test

conn = mysql.connector.connect(
        host=db_connector_test.PY_HOST, 
        database=db_connector_test.PY_DB_NAME, 
        user=db_connector_test.PY_USERNAME, 
        password=db_connector_test.PY_PASSWORD
    )

if conn.is_connected():
    print('Connection Established to DB')

cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO emp VALUES(3, 'Bob Master', 23500)")
    conn.commit()
    print("Employee added.")
except:
    conn.rollback()
    print('Something went wrong')

cursor.close()
conn.close()