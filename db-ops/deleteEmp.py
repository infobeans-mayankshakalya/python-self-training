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
        cursor.execute("DELETE FROM emp WHERE id='%d'" % (3))
        conn.commit()
        print("Employee deleted.")
    except:
        conn.rollback()
        print('Something went wrong')
    finally:
        cursor.close()
        conn.close()