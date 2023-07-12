/*Selecionando coluna email e state onde é igual a Santa Catarina*/
SELECT email, state FROM sales.customers WHERE state='SC';

/*Selecionando emails dos clientes onde são de Santa Catarina e Mato Grosso do Sul*/
SELECT email, state FROM sales.customers WHERE state='SC' or state ='MS';

/*Selecionando emails de clientes de SC e MS que tem mais de 30 anos*/
SELECT email, state, birth_date FROM sales.customers
WHERE (state = 'SC' or state = 'MS') and birth_date < '1993-07-09'