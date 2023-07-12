/*Alterando nome da coluna*/
alter table sales.customers
rename column customers_age to age

select * from sales.customers

/*inserindo valores em uma coluna*/
update  sales.customers
set customers_age = datediff('y',birth_date,current_date)
where true

/*Alterando o tipo de uma coluna*/
alter table sales.customers
add customers_age int

/*Inserindo valores em uma tabela nova*/
update  sales.customers
set idade = datediff('y',birth_date,current_date)
where true

/*Deletando uma coluna*/
alter table sales.customers
drop column idade