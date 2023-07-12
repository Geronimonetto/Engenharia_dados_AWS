/**/
SELECT * FROM sales.products 
WHERE price > (SELECT MIN(price) 
FROM sales.products) 
GROUP BY product_id
ORDER BY price DESC;

/*Calcular a idade média dos clientes por professional_status*/
WITH tabela_nova as (
SELECT
	professional_status,
	(CURRENT_DATE - birth_date)/360 as idade
FROM sales.customers

)
SELECT 
	professional_status,
	AVG(idade) as idade_media
FROM tabela_nova
GROUP BY professional_status;

/*Calcular a idade média dos clientes por status profissional*/
SELECT 
	professional_status,
	avg(idade) as idade_media
FROM (
	SELECT 
		professional_status,
		(CURRENT_DATE - birth_date)/365 as idade
	FROM sales.customers
) as tabela_nova
GROUP BY professional_status;

/*Na tabela sales.funnel crie uma coluna que informe o nª 
de visitar acumuladas que a loja visitada recebeu até o momento*/
SELECT
	fun.visit_id,
	fun.visit_page_date,
	sto.store_name,
	(
		SELECT count(*)
		FROM sales.funnel as fun2
		WHERE fun2.visit_page_date <= fun.visit_page_date
		and fun.store_id = fun2.store_id
	) as visitasacumuladas

FROM sales.funnel as fun
LEFT JOIN sales.stores as sto
	ON fun.store_id = sto.store_id
ORDER BY sto.store_name, fun.visit_page_date
	
	
