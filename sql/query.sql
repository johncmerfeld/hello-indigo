SELECT
  COUNT(*),
  e.team_id
FROM
  employee as e
INNER JOIN test as t on
  t.tested_by_employee_id = e.id
WHERE t.average_cfu_per_seed IS NOT NULL
AND t.date_plated_on BETWEEN '2020-09-01' AND '2020-10-01'
GROUP BY e.team_id
