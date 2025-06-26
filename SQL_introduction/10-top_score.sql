-- Liste tous les enregistrements de la table second_table par score (du meilleur au moins bon).
-- Affiche uniquement le score et le nom.
SELECT score, name
FROM second_table
ORDER BY score DESC;
