from uuid import UUID
from nomadbook.model.Viagem import Viagem

def create_viagem(conn, titulo: str, descricao: str, created_by: UUID):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO viagem (titulo, descricao, created_at, updated_at, created_by)
            VALUES (%s, %s, NOW(), NOW(), %s)
            RETURNING id
            """,
            (titulo, descricao, created_by)
        )
        viagem_id = cur.fetchone()["id"]  # Retorna o id da nova viagem
        return viagem_id


def get_viagem_by_id(conn, viagem_id: UUID):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT id, titulo, descricao, created_at, updated_at, created_by
            FROM viagem
            WHERE id = %s
            """,
            (viagem_id,)
        )
        return cur.fetchone()  # Retorna um dicionário com os detalhes da viagem


def get_all_viagens(conn):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT id, titulo, descricao, created_at, updated_at, created_by
            FROM viagem
            """
        )
        return cur.fetchall()  # Retorna uma lista de dicionários


def update_viagem(conn, viagem_id: UUID, novo_titulo=None, nova_descricao=None):
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE viagem
            SET
                titulo = COALESCE(%s, titulo),
                descricao = COALESCE(%s, descricao),
                updated_at = NOW()
            WHERE id = %s
            """,
            (novo_titulo, nova_descricao, viagem_id)
        )


def delete_viagem(conn, viagem_id: UUID):
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE viagem
            SET updated_at = NOW(), deleted_at = NOW()
            WHERE id = %s
            """,
            (viagem_id,)
        )
