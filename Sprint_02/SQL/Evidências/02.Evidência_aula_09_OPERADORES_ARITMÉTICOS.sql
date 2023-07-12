/* Concatenando duas colunas ou mais */
SELECT CONCAT(first_name, ' ', last_name ) as "Nome Completo" FROM sales.customers;
SELECT first_name || ' ' || last_name as "Nome Completo" FROM sales.customers;

/* Na aula 09 foi mencionado o || para concatenar colunas porém existe também o comando CONCAT que 
pode ser utilizado para unir 2 ou mais colunas*/