/*Contando quantidade de clientes agrupados por estados*/
SELECT state, COUNT(*) as contando 
FROM sales.customers
GROUP BY state
ORDER BY contando DESC;

/*Contando o número de clientes por estado e status profissional*/
SELECT state, professional_status, count(*) as contagem FROM sales.customers
GROUP BY state, professional_status
ORDER BY state, contagem DESC;

SELECT state, professional_status, count(*) as contagem FROM sales.customers
GROUP BY 1,2
ORDER BY state, contagem DESC;

SELECT state FROM sales.customers GROUP BY state 
/* O GROUP BY pode ser também usado como um DISTINCT*/

