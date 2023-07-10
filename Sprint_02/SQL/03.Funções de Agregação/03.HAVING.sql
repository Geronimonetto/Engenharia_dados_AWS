/*Contando estados com mais de 100 clientes*/
SELECT state, count(*) as contagem FROM sales.customers
GROUP BY state
HAVING count(*) > 100 and state <> 'MG'
ORDER BY contagem DESC


