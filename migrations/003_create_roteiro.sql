CREATE TABLE roteiro (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    viagem_id   UUID NOT NULL REFERENCES viagem(id),
    dia         DATE NOT NULL,
    lugar       VARCHAR(100) NOT NULL,
    atividade   TEXT NOT NULL,
    created_at  TIMESTAMP NOT NULL DEFAULT now(),
    updated_at  TIMESTAMP NOT NULL DEFAULT now(),
    deleted_at  TIMESTAMP
);