/* OPERADORES LÓGICOS 
- AND - Mais de uma condição
- OR - Uma condição ou outra
- NOT - Inverte a condição
- BETWEEN - Está entre
- IN - Está em
- LIKE - Como
- ILIKE - 
- IS NULL - Não é nulo
*/

/*Selecionando os produtos entre 100000 e 200000 com BETWEEN*/
SELECT * FROM sales.products
WHERE price BETWEEN 100000 and 200000;

/*Selecionando produtos com preço que não estão entre 100000 e 200000 com NOT*/
SELECT * FROM sales.products
WHERE price NOT BETWEEN 100000 and 200000;

/*Selecionando os produtos de marcas com IN*/
SELECT * FROM sales.products
WHERE brand IN ('HONDA','TOYOTA','RENAULT');
/*Invervendo com NOT*/
SELECT * FROM sales.products
WHERE brand NOT IN ('HONDA','TOYOTA','RENAULT');

/*Selecionando os nomes que iniciam ou terminam com algum texto ou nome específico com LIKE*/
SELECT DISTINCT first_name FROM sales.customers
WHERE first_name LIKE 'GER%';

/*Selecionando os nomes de acordo com o filtro e além disso independente das 
letra serem maiúsculas ou minúsculas*/
SELECT DISTINCT CONCAT(first_name, ' ', last_name) as nomecompleto FROM sales.customers
WHERE first_name ILIKE 'ger%';

/*Selecionando os campos NULOS com IS NULL*/
SELECT * FROM schema.coluna WHERE campo IS NULL;










