/* Ordenando Coluna produtos em ordem de preços */
SELECT * FROM sales.products ORDER BY price;

/* Ordenando Coluna produtos em ordem de preços de forma decrescente */
SELECT * FROM sales.products ORDER BY price DESC;

/* Ordenando Coluna State da tabela customers em ordem de letra */
SELECT DISTINCT state FROM sales.customers ORDER BY state;