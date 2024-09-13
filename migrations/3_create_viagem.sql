CREATE TABLE viagem (
   id        UUID PRIMARY KEY DEFAULT gen_random_uuid(),
   titulo      TEXT NOT NULL UNIQUE
)