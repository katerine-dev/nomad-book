# Return a connection provided by psycopg.
import psycopg

def get_connection():
    return psycopg.connect(
        "dbname=nomadbook host=localhost user=nomadbook password=nomadbook port=5432", autocommit=True
    )