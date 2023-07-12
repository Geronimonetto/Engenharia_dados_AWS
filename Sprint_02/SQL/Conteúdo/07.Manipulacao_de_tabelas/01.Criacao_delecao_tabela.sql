/*Criando uma tabela de aniversário com o select a partir de outra tabela*/
select 
	customer_id,
	datediff('y', birth_date, current_date)
	into temp_tables.customers_age
from sales.customers

select *
from temp_tables.customers_age

/* Criação de tabela com a tradução a partir do zero dos status profissionais dos clientes */

select
	distinct professional_status
from sales.customers

create table temp_tables.profissoes(
	professional_status varchar,
	status_profissional varchar

)

insert into temp_tables.profissoes
(professional_status, status_profissional)

values
('Freelancer','Freelancer'),
('Retired', 'Aposentado'),
('CLT', 'Carteira Assinada'),
('Self_employed', 'Autônomo'),
('Businessman','Empresário'),
('Civil_servant','Funcionário Público'),
('Student','Estudante')

select *
from temp_tables.profissoes

/*Deletando tabelas*/

drop tables temp_tables.profissoes