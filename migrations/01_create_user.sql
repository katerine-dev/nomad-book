CREATE TABLE user (
   id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
   email      TEXT NOT NULL UNIQUE,
   nome       TEXT NOT NULL,
   user       TEXT NOT NULL UNIQUE,
   senha      TEXT
);