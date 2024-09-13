CREATE TABLE roteiro (
   id        UUID NOT NULL UNIQUE,
   dia       DATE,
   lugar     varchar(100),
   atividade TEXT,
   FOREIGN KEY (id) REFERENCES viagem(id),
   updated_at TIMESTAMP NOT NULL DEFAULT now(),
   deleted_at TIMESTAMP
)