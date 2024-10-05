from uuid import UUID
from nomadbook.model.Roteiro import Roteiro

def create_roteiro(conn, viagem_id: UUID, dia: str, lugar: str, atividade: str):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO roteiro (viagem_id, dia, lugar, atividade, created_at, updated_at)
            VALUES (%s, %s, %s, %s, NOW(), NOW())
            RETURNING id
            """,
            (viagem_id, dia, lugar, atividade)
        )
        roteiro_id = cur.fetchone()["id"]  # Retorna o id do novo roteiro
        return roteiro_id


def get_roteiro_by_id(conn, roteiro_id: UUID):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT id, viagem_id, dia, lugar, atividade, created_at, updated_at
            FROM roteiro
            WHERE id = %s
            """,
            (roteiro_id,)
        )
        return cur.fetchone()  # Retorna um dicionário com os detalhes do roteiro


def get_all_roteiros(conn):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT id, viagem_id, dia, lugar, atividade, created_at, updated_at
            FROM roteiro
            """
        )
        return cur.fetchall()  # Retorna uma lista de dicionários


def update_roteiro(conn, roteiro_id: UUID, novo_dia=None, novo_lugar=None, nova_atividade=None):
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE roteiro
            SET
                dia = COALESCE(%s, dia),
                lugar = COALESCE(%s, lugar),
                atividade = COALESCE(%s, atividade),
                updated_at = NOW()
            WHERE id = %s
            """,
            (novo_dia, novo_lugar, nova_atividade, roteiro_id)
        )


def delete_roteiro(conn, roteiro_id: UUID):
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE roteiro
            SET updated_at = NOW(), deleted_at = NOW()
            WHERE id = %s
            """,
            (roteiro_id,)
        )
