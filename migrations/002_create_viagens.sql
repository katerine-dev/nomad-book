CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE viagens (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    titulo      TEXT NOT NULL UNIQUE,
    descricao   TEXT,
    created_at  TIMESTAMP NOT NULL DEFAULT now(),
    updated_at  TIMESTAMP NOT NULL DEFAULT now(),
    created_by  UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE
);