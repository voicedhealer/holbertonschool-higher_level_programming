-- Liste les enregistrements avec un score >= 10 dans la table second_table.
-- Affiche le score et le nom, triés par score décroissant.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
