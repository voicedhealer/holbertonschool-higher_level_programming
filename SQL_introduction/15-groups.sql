-- Liste le nombre d'enregistrements avec le même score dans second_table.
-- Affiche le score et le nombre d'enregistrements pour ce score, étiqueté 'number'.
-- Trie par le nombre d'enregistrements (décroissant).
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
