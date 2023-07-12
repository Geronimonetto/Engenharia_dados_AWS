/* (Exercício 1) Identifique quais as marcas de veículo 
mais visitada na tabela sales.funnel*/

SELECT 
	brand,
	COUNT(visit_page_date)
FROM sales.products as car 
LEFT JOIN sales.funnel as fun
	ON car.product_id = fun.product_id
GROUP BY brand
ORDER BY brand;

/*(Exercício 2) Identifique quais as lojas de veículo mais visitadas 
na tabela sales.funnel*/

SELECT
	lojas.store_name,
	COUNT(visit_page_date) as contagem
FROM sales.stores as lojas
LEFT JOIN sales.funnel as fun
	ON lojas.store_id = fun.store_id
GROUP BY store_name
ORDER BY contagem DESC;

/*(Exercício 3) Identifique quantos clientes moram em cada tamanho de cidade (o porte da cidade
consta na coluna "size" da tabela temp_tables.regions)*/
SELECT
	reg.size,
	COUNT(*) AS contagem
FROM sales.customers AS cli
LEFT JOIN temp_tables.regions AS reg
	ON lower(cli.city) = lower(reg.city)
	and lower(cli.state) = lower(reg.state)
GROUP BY reg.size
ORDER BY contagem;




