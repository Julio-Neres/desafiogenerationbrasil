CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    idade INTEGER,
    nota_primeiro_semestre DECIMAL(4, 2),
    nota_segundo_semestre DECIMAL(4, 2),
    nome_professor VARCHAR(255),
    numero_sala VARCHAR(10)
);