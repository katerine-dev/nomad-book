from nomadbook.model.Usuario import Usuario

def create_usuario(conn, email: str, nome: str, senha: str):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO usuario (email, nome, senha, created_at, updated_at)
            VALUES (%s, %s, %s, NOW(), NOW())
            RETURNING id
            """,
            (email, nome, senha)
        )
        usuario_id = cur.fetchone()["id"] # Só está retornando assim pq agora a conexão passou a retornar uma lista de dicionários
        return usuario_id
      
def get_usuario_by_id(conn, usuario_id):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT id, email, nome, senha, created_at, updated_at
            FROM usuario
            WHERE id = %s
            """,
            (usuario_id,)
        )
        return cur.fetchone()  # Retorna um dicionário
    

def get_all_usuarios(conn):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT id, email, nome, senha, created_at, updated_at
            FROM usuario
            """
        )
        return cur.fetchall()  # Retorna uma lista de dicionários

def update_usuario(conn, usuario_id, novo_email=None, novo_nome=None, nova_senha=None):
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE usuario
            SET
                email = COALESCE(%s, email),
                nome = COALESCE(%s, nome),
                senha = COALESCE(%s, senha),
                updated_at = NOW()
            WHERE id = %s
            """,
            (novo_email, novo_nome, nova_senha, usuario_id)
        )


# Obs: COALESCE permite que atualize apenas os campos fornecidos sem precisar construir dinamicamente a consulta SQL

def delete_usuario(conn, usuario_id):
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE usuario
            SET updated_at = NOW(), deleted_at = NOW()
            WHERE id = %s
            """,
            (usuario_id,)
        )