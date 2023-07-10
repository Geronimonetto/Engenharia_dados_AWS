/*Tipos de comandos para subqueries*/

-- WHERE
-- WITH
-- FROM
-- SELECT

/*Exemplo 01*/

SELECT * FROM sales.products WHERE price = (SELECT MIN(price) FROM sales.products);

/*(Exemplo 02)Calcule a idade média dos clientes por status profissional*/
WITH alguma_tabela as (

)
select 
	professional_status,
	AVG((CURRENT_DATE - birth_date)/365)
FROM sales.customers
GROUP BY professional_status
