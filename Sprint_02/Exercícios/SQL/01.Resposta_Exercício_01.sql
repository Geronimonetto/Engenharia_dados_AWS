/*Resposta 01*/
SELECT DISTINCT city as cidades FROM sales.customers WHERE state='MG' ORDER BY city;

/*Resposta 02*/
SELECT visit_id FROM sales.funnel WHERE paid_date is not null ORDER BY paid_date DESC LIMIT 10;


/*Resposta 03*/
SELECT * FROM sales.customers WHERE birth_date >= '20000101' ORDER BY score DESC LIMIT 10;