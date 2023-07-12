/*Inserindo valores na tabela*/

insert into temp_tables.profissoes (
professional_status, status_profissional
)

values
('Trainee', 'Estagiário'),
('unemployed', 'Desempregado')

select * from temp_tables.profissoes

/*Atualizando linha (valores) da tabela*/

update temp_tables.profissoes
set professional_status = 'intern'
where status_profissional = 'Estagiário'

select * from temp_tables.profissoes

/*Deletando Linhas*/

delete from temp_tables.profissoes
where status_profissional = 'Estagiário'
or status_profissional = 'Desempregado'

