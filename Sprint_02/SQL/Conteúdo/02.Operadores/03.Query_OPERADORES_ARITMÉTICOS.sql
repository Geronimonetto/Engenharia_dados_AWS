/* Selecionando clientes e a idade */
SELECT first_name, birth_date,(current_date - birth_date)/365 AS "idade do cliente"
FROM sales.customers;

/*Selecionando os 10 clientes mais novos*/
SELECT first_name, birth_date,(current_date - birth_date)/365 AS "idade do cliente"
FROM sales.customers ORDER BY "idade do cliente" LIMIT 10;

/* Concatenando duas colunas de textos*/
SELECT CONCAT(first_name,' ',last_name) FROM sales.customers;
SELECT (first_name || ' ' || last_name) as "Nome Completo" FROM sales.customers;

