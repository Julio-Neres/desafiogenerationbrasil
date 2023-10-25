CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INTEGER NOT NULL,
    nota_semestre1 FLOAT NOT NULL,
    nota_semestre2 FLOAT NOT NULL,
    nome_professor VARCHAR(100) NOT NULL,
    sala VARCHAR(20) NOT NULL
);
