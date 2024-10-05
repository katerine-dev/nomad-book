# Return a connection provided by psycopg.
import psycopg
from psycopg.rows import dict_row

# psycopg sempre irá retornar um dicionário e aqui estamos fazendo retornar para pydentic (validação de dados)
def get_connection():
    conn = psycopg.connect(
        "dbname=nomadbook host=localhost user=nomadbook password=nomadbook port=5432",
        autocommit=True,
        row_factory=dict_row
    )
    return conn