CREATE TABLE viagem (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    titulo      TEXT NOT NULL UNIQUE,
    descricao   TEXT NOT NULL,
    created_at  TIMESTAMP NOT NULL DEFAULT now(),
    updated_at  TIMESTAMP NOT NULL DEFAULT now(),
    created_by  UUID NOT NULL REFERENCES usuario(id),
    deleted_at TIMESTAMP
);