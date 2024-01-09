DROP table if exists pokedex.kpis;

CREATE SCHEMA pokedex;

CREATE TABLE pokedex.random_appears (
  pokemon VARCHAR(100) NOT NULL,
  "level" INTEGER NOT NULL,
  health INTEGER NOT NULL,
  attack INTEGER NOT NULL,
  defense INTEGER NOT NULL,
  ts_appear TIMESTAMP
);