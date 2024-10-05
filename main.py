from nomadbook.db import connection as db_connection


conn = db_connection.get_connection()
cur = conn.cursor()
