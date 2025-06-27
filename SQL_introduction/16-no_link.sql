-- Ce script liste les enregistrements de la table second_table
-- en excluant ceux dont le nom est NULL ou vide, triés par score.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
