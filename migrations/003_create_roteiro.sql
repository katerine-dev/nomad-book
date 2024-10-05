CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE roteiros (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    viagem_id   UUID NOT NULL REFERENCES viagens(id) ON DELETE CASCADE,
    dia         DATE NOT NULL,
    lugar       VARCHAR(100) NOT NULL,
    atividade   TEXT NOT NULL,
    created_at  TIMESTAMP NOT NULL DEFAULT now(),
    updated_at  TIMESTAMP NOT NULL DEFAULT now(),
    deleted_at  TIMESTAMP
);