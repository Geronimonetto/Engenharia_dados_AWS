/* Tipos de funções agregadas */
-- COUNT() - Contando linhas
-- SUM() - Soma
-- MIN() - Menor valor
-- MAX() - Maior valor
-- AVG() - Média

/*Contando quantidade de linhas da tabela funnel*/
SELECT COUNT(*) FROM sales.funnel;

/*Contando quantidade de pagamentos da tabela funnel*/
SELECT COUNT(paid_date) FROM sales.funnel;

/*Contando quantidade de produtos em janeiro*/
SELECT COUNT(DISTINCT(product_id)) FROM sales.funnel 
WHERE visit_page_date BETWEEN '20210101' and '20210131';

/*Selecionando menor valor, maior valor e média*/
SELECT MIN(price), MAX(price), AVG(price) FROM sales.products;

/*Selecionando o produto mais caro com subquery*/
SELECT * FROM sales.products WHERE price = (SELECT MAX(price) FROM sales.products);
