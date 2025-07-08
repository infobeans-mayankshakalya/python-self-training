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
cursor.execute("select * from emp")

# row = cursor.fetchone()

# while row is not None:
#     print('row:', row)
#     row = cursor.fetchone()

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()