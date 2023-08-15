-- List all records of table second_table (excluding rows without a name value)
-- Display score and name, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
